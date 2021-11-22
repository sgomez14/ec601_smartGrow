#include "pwm_functions.h"

/* Struct used to monitor system health */
power_consumption system_device_health;
Adafruit_INA260 ina260 = Adafruit_INA260();

/* {Pin Number, min voltage, max voltage} */
PWM_device water_pump_source = { 36, 145, 255};
PWM_device water_pump_drain = { 15, 180, 255};
PWM_device food_pump = { 33, 180, 255};
PWM_device air_pump = { 14, 230, 255};
PWM_device LED = { 37, 145, 255};
String command_packet = "";
DHT temp_sensor(DHTPIN, DHTTYPE);

/* Variables for timers. */
elapsedMillis change_water;
elapsedMillis turn_on_light;
elapsedMillis turn_off_light;

/* Networking Variable */
bool response_requested = true;
byte mac[] = {
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00
};
int local_port = 8888;
EthernetUDP Udp;
int server_port = 8888;
IPAddress server_IP(192, 168, 0, 0);
IPAddress device_ip(192, 168, 0, 1);

/* Info on multifile variables: 
https://stackoverflow.com/questions/1433204/how-do-i-use-extern-to-share-variables-between-source-files

Demo: Water changes after 1 minute, light turns off after 1.5 minutes, turns back on after 2 minutes. */
unsigned int change_water_threshold = 15000;
unsigned int turn_on_light_threshold = 23000; /* After how long to turn the light back on, when in off state. */
unsigned int turn_off_light_threshold = 10000; /* After how long to turn light off, when in on state.*/

uint8_t dosage = 0;

unsigned long time_to_fill = 35000; /* milliseconds */

bool tank_is_full_flag = 0;
bool LED_status = 0;

/* Use PWM_Calibration to find the operating range for your motors and devices. This is used to set up your PWM_device structs' min and max value. */
void PWM_calibration(PWM_device *pwm_device)
{
	/* Making local copies for code readability. */
	uint8_t gpio_pin, min, max;
	gpio_pin = pwm_device->pin;
	min = pwm_device->min;
	max = pwm_device->max;
	
	/* Runs through entire operating range for PWM device. */
	for (int i = min; i <= max; i += 5) {
		analogWrite(gpio_pin, i);
		delay(100);
	}
	for (int i = max; i >= min; i -= 5) {
		analogWrite(gpio_pin, i);
		delay(100);
	}

	/* Ensures PWM device is off at end of function. */
	analogWrite(gpio_pin,0);
}

/* Sets a PWM device to a specific pulse width, determined by percent. 0% turns off device, and 100% turns it to the device's max. */
void PWM_set_percent(PWM_device *pwm_device, uint8_t percent)
{
	/* Making local copies for code readability. */
	uint8_t gpio_pin, min, max, pulse_width, working_range;
	gpio_pin = pwm_device->pin;
	min = pwm_device->min;
	max = pwm_device->max;
	working_range = max - min;

	/* If percent is 0, turn device off. */
	if (percent == 0)
	{
		analogWrite(gpio_pin, 0);
	}
	/* If percent is 100, turn device to max. */
	else if (percent == 100)
	{
		analogWrite(gpio_pin, max);
	}
	/* In between, calculate pulse_width based on offset and percent of max working range for the specific pump. */
	else if ((percent < 100) && (percent > 0)) {
		pulse_width = min + ((percent/100) * working_range);
		analogWrite(gpio_pin, pulse_width);
	}
	else
	{
		Serial.println("Parameter Error: Outside range (0 - 100).");
		return;
	}
	return;
}

/* Doses food from a food source via a small (~250 ms) delay based on mL input. Needs the global macro FILL_RATE set depending on physical system measurements. */
void dose_food(PWM_device *pwm_device, uint8_t ml)
{
	/* Making local copies for code readability. */
	/* dose_run_time is in milliseconds. */
	uint32_t dose_run_time;
	uint8_t gpio_pin, min, max, pulse_width, working_range;
	gpio_pin = pwm_device->pin;
	min = pwm_device->min;
	max = pwm_device->max;
	working_range = max - min;

	dose_run_time = 1000*(ml / FILL_RATE); //(ml / (ml/s) == ml * (s/ml)
	/* Printing for debug */
	Serial.print("dose_run_time: ");
	Serial.println(dose_run_time);

	/* Setting 10% duty cycle for more accurate dosing. Compiler should simplify this. */
	pulse_width = min + ((10 / 100) * working_range);

	//Need to do: Calibrate pump by measuring how long it takes to does 100 ml of water.

	/* Starts pump for time based on dose_run_time. */
	Serial.println("Timer Started.");
	analogWrite(gpio_pin, pulse_width);
	delay(dose_run_time);
	Serial.println("Timer Expired.");
	analogWrite(gpio_pin, 0);

	return;
}	

/* Starts to fill the tank. Process also includes detecting if the planter tank is full, and measures how long it took. */
void fill_tank(PWM_device* pwm_device)
{
	/* Time between start and stop of pumping. */
	PWM_set_percent(pwm_device, 80);
	delay(time_to_fill);
	PWM_set_percent(pwm_device, 0);
	tank_is_full_flag = 1;
}

/* Starts to empty the tank. Uses the fill time and a constant scalar to calculate how long it will take to empty the tank.  */
void empty_tank(PWM_device* pwm_device) 
{
	unsigned long time_to_empty = time_to_fill  * 1.1;
	PWM_set_percent(pwm_device, 80);
	delay(time_to_empty);
	PWM_set_percent(pwm_device, 0);
	tank_is_full_flag = 0;
}

/* Given a LED PWM_device, toggles the light on or off depending on current state of the light.  */
void toggle_light(PWM_device* pwm_device)
{
	/* If pin is HIGH, i.e. light is on... */
	if (LED_status == 1)
	{
		Serial.println("Turning light off...");
		PWM_set_percent(pwm_device, 0);
		LED_status = 0;
	}

	/* If pin is low, i.e. light is off... */
	else if (LED_status == 0)
	{
		Serial.println("Turning light on...");
		PWM_set_percent(pwm_device, 100);
		LED_status = 1;
	}

	/* Error catch */
	else
	{
		Serial.println("Error toggling LED!!");
	}
}

/* Resets the system, setting all devices off. */
void reset()
{
	PWM_set_percent(&water_pump_source, 0);
	PWM_set_percent(&water_pump_drain, 0);
	PWM_set_percent(&food_pump, 0);
	PWM_set_percent(&air_pump, 0);
	PWM_set_percent(&LED, 0);
	change_water = 0;
	turn_on_light = 0;
	turn_off_light = 0;
}

/* Sets up the system. Turns LED & air pump on. */
void initialize()
{
	fill_tank(&water_pump_source);
	toggle_light(&LED);
	PWM_set_percent(&air_pump, 100);
}

void scheduler()
{
	if (change_water >= change_water_threshold) {
		Serial.println("Changing water!");
		Serial.print("Time to fill before drain: ");
		Serial.println(time_to_fill);
		empty_tank(&water_pump_drain);
		delay(1000);
		fill_tank(&water_pump_source);
		Serial.print("Time to fill after refilling: ");
		Serial.println(time_to_fill);
		delay(1000);
		//dose_food(&food_pump, 5);
		change_water = 0;
	}
	if ((turn_off_light >= turn_off_light_threshold) && LED_status) {
		Serial.println("Turning off light!");
		toggle_light(&LED);
		turn_off_light = 0;
		turn_on_light = 0;
	}
	if ((turn_on_light >= turn_on_light_threshold) && !LED_status) {
		Serial.println("Turning on light!");
		toggle_light(&LED);
		turn_on_light = 0;
		turn_off_light = 0;
	}
}

/* Gets instruction packet via UDP from server. */
void get_packet()
{
	const int input_packet_size = 5; /* Size of buffer in bytes*/
	byte input_packet_buffer[input_packet_size];

	if (Udp.parsePacket()) 
	{
		// We've received a packet, read the data from it
		Udp.read(input_packet_buffer, input_packet_size);

		if (bitRead(input_packet_buffer[0], 0) == 0)
		{
			response_requested = true;
		}
		else if ((bitRead(input_packet_buffer[0], 0) == 1))
		{
			/* Parse incoming packet. Reads the nth byte of the input packet as an uint8_t. */
			change_water_threshold =	(uint8_t)input_packet_buffer[1];
			turn_on_light_threshold =	(uint8_t)input_packet_buffer[2];
			turn_off_light_threshold =	(uint8_t)input_packet_buffer[3];
			dosage =					(uint8_t)input_packet_buffer[4];
			response_requested = false;
		}
		else
		{
			Serial.println("ERROR: Bad UDP packet!");
			response_requested = false;
		}


	}
}

/* Sends response packet via UDP to server. */
void send_packet()
{ 
	if (response_requested == true)
	{
		/* We need an output packet for 5 32-bit values. So 5 x 4 bytes = 20 bytes. */
		const int output_packet_size = 21; /* bytes */
		char output_string[21];
		byte output_packet_buffer[output_packet_size];
		uint32_t voltage, current, temp, humidity, luminosity;
		uint8_t pump_status;

		memset(output_packet_buffer, 0, sizeof(output_packet_buffer));

		voltage =		0xBBBBBBBB;//ina260.readBusVoltage();
		current =		0xCCCCCCCC;//ina260.readCurrent();
		temp =			0xDDDDDDDD;//temp_sensor.readTemperature();
		humidity =		0xEEEEEEEE;//temp_sensor.readHumidity();
		luminosity =	0xFFFFFFFF;
		/* bit mask for pump status */
		pump_status =	0xAA;

		//Serial.printf("Measured Temp: %f\nMeasured Humidity: %f\n", temp_sensor.readTemperature() , temp_sensor.readHumidity());
		//Serial.printf("Stored Temp: %f\nStored Humidity: %f\n", temp, humidity);

		memcpy((output_string + 0), &voltage, 4);
		memcpy((output_string + 4), &current, 4);
		memcpy((output_string + 8), &temp, 4);
		memcpy((output_string + 12), &humidity, 4);
		memcpy((output_string + 16), &luminosity, 4);
		memcpy((output_string + 20), &pump_status, 1);


#if DEBUG
		Serial.print("Output buffer: ");
		for (int i = 0; i < output_packet_size; i++)
		{
			Serial.printf("%x", output_string[i]);
		}
		Serial.println("");
#endif

#if ETHERNET
		Udp.beginPacket(server_IP, server_port);
		Udp.write(output_string, output_packet_size);
		Udp.endPacket();
#endif
		response_requested == false;
	}
}

/* Calculates baseline power draw from various PWM devices. Used to monitor system health. */
void calibrate_power_draw()
{
	reset();
	PWM_set_percent(&water_pump_source, 100);
	system_device_health.source_current = ina260.readCurrent();
	reset();
	PWM_set_percent(&water_pump_drain,100);
	system_device_health.drain_current = ina260.readCurrent();
	reset();
	PWM_set_percent(&food_pump, 100);
	system_device_health.food_current = ina260.readCurrent();
	reset();
	PWM_set_percent(&LED, 100);
	system_device_health.light_current = ina260.readCurrent();
	reset();
}

/* Finds Teensy MAC address and populates local MAC address buffer (6 bytes). Sourced from:
   https://forum.pjrc.com/threads/62932-Teensy-4-1-MAC-Address
*/
void teensyMAC(uint8_t* mac) {
	for (uint8_t by = 0; by < 2; by++) mac[by] = (HW_OCOTP_MAC1 >> ((1 - by) * 8)) & 0xFF;
	for (uint8_t by = 0; by < 4; by++) mac[by + 2] = (HW_OCOTP_MAC0 >> ((3 - by) * 8)) & 0xFF;
	Serial.printf("MAC: %02x:%02x:%02x:%02x:%02x:%02x\n", mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
}
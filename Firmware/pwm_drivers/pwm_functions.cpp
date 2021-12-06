#include "pwm_functions.h"

/* Struct used to monitor system health */
power_consumption system_device_health;
Adafruit_INA260 ina260 = Adafruit_INA260();

#define GROWPOD_NUMBER 2

/* {Pin Number, min voltage, max voltage} */
/* Growpod 1 Settings */
#if GROWPOD_NUMBER == 1
	PWM_device water_pump_source = { 36, 145, 255,0 };
	PWM_device water_pump_drain = { 15, 145, 255,0 };
	PWM_device food_pump = { 33, 180, 255,0 };
	PWM_device air_pump = { 14, 230, 255,0 };
	PWM_device LED = { 37, 145, 255,0 };
	String command_packet = "";
#endif

/* Growpod 2 Settings */
#if GROWPOD_NUMBER == 2
	PWM_device water_pump_source = { 36, 145, 255,0};
	PWM_device water_pump_drain = { 15, 145, 255,0};
	PWM_device food_pump = { 33, 180, 255,0};
	PWM_device air_pump = { 14, 230, 255,0};
	PWM_device LED = { 37, 145, 255,0};
	String command_packet = "";
#endif

/* Growpod 3 Settings */
#if GROWPOD_NUMBER == 3
	PWM_device water_pump_source = { 36, 180, 255,0 };
	PWM_device water_pump_drain = { 15, 180, 255,0 };
	PWM_device food_pump = { 33, 180, 255,0 };
	PWM_device air_pump = { 14, 230, 255,0 };
	PWM_device LED = { 37, 145, 255,0 };
	String command_packet = "";
#endif

/* Variables for timers. */
elapsedMillis change_water;
elapsedMillis turn_on_light;
elapsedMillis turn_off_light;

/* Networking Variable */
bool response_requested = false;
byte mac[] = {
#if GROWPOD_NUMBER == 1
  //mac for growPod1
  0x04, 0xe9, 0xe5, 0x10, 0x30, 0x77
#endif

 #if GROWPOD_NUMBER == 2
  //mac for growPod2
  0x04, 0xe9, 0xe5, 0x0e, 0xcf, 0x0c
#endif

#if GROWPOD_NUMBER == 3
  //mac for growPod3
  0x04, 0xe9,0xe5,0x10,0x7d,0xa2
#endif
};

int local_port = 80;
EthernetUDP Udp;
int server_port = 80;
IPAddress server_IP(192, 168, 0, 100);

#if GROWPOD_NUMBER == 1
//ip for growPod1
IPAddress device_ip(192, 168, 0, 101);
#endif

#if GROWPOD_NUMBER == 2
//ip for growPod2
IPAddress device_ip(192, 168, 0, 102);
#endif

#if GROWPOD_NUMBER == 3
//ip for growPod3
IPAddress device_ip(192, 168, 0, 103);
#endif

/* Info on multifile variables: 
https://stackoverflow.com/questions/1433204/how-do-i-use-extern-to-share-variables-between-source-files

Demo: Water changes after 10 minute, light turns off after 15 minutes, turns back on after 20 minutes. */
unsigned int change_water_threshold = 0xFFFFFFFF;
unsigned int turn_on_light_threshold = 0xFFFFFFFF; /* After how long to turn the light back on, when in off state. */
unsigned int turn_off_light_threshold = 0xFFFFFFFF; /* After how long to turn light off, when in on state.*/

uint8_t dosage = 0;

unsigned long time_to_fill = 35000; /* milliseconds */
bool system_attention_flag = 0;
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
    pwm_device -> motor_status = 0;
    
	}
	/* If percent is 100, turn device to max. */
	else if (percent == 100)
	{
		analogWrite(gpio_pin, max);
    pwm_device -> motor_status = 1;
	}
	/* In between, calculate pulse_width based on offset and percent of max working range for the specific pump. */
	else if ((percent < 100) && (percent > 0)) {
		pulse_width = min + ((percent/100) * working_range);
		analogWrite(gpio_pin, pulse_width);
    pwm_device -> motor_status = 1;
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
  PWM_set_percent(&food_pump, 50);
  delay(1500);
  PWM_set_percent(&food_pump, 0);
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
	unsigned long time_to_empty = time_to_fill  * 1.05;
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
	Serial.println("RESETTING!");
	PWM_set_percent(&water_pump_source, 0);
	PWM_set_percent(&water_pump_drain, 0);
	PWM_set_percent(&food_pump, 0);
	PWM_set_percent(&air_pump, 0);
	PWM_set_percent(&LED, 0);
	LED_status = 0;
	change_water = 0;
	turn_on_light = 0;
	turn_off_light = 0;
	change_water_threshold = 0xFFFFFFFF;
	turn_on_light_threshold = 0xFFFFFFFF;
	turn_off_light_threshold = 0xFFFFFFFF;
}

/* Sets up the system. Turns LED & air pump on. */
void initialize()
{
	Serial.println("In init!");
	PWM_set_percent(&air_pump, 100);
	toggle_light(&LED);
	Serial.println(air_pump.motor_status);
	empty_tank(&water_pump_drain);
	fill_tank(&water_pump_source);
	
}

void scheduler()
{
	if (change_water >= change_water_threshold) {
		Serial.println("Changing water!");
		empty_tank(&water_pump_drain);
		delay(1000);
		fill_tank(&water_pump_source);
		delay(1000);
		dose_food(&food_pump, 5);
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
	const int input_packet_size = 128; /* Size of buffer in bytes*/
	char input_packet_buffer[input_packet_size];
	unsigned int new_water_schedule, new_light_on_schedule, new_light_off_schedule;
	float new_dosage;
	char command_packet[6];

	if (Udp.parsePacket()) 
	{
		// We've received a packet, read the data from it
		Udp.read(input_packet_buffer, input_packet_size);

		Serial.printf("Input packet: %s\n", input_packet_buffer);

		/* sscanf needs \n ? */
		sscanf(input_packet_buffer, "%s %u %f %u %u", command_packet, &new_water_schedule, &new_dosage, &new_light_on_schedule,&new_light_off_schedule);

		Serial.printf("New Variables:\nCommand: %s|\nNew Water Schedule: %hhu\nNew Dosage: %f\nNew light on: %hhu\nNew light off: %hhu\n", command_packet, new_water_schedule, new_dosage, new_light_on_schedule, new_light_off_schedule);


		if (strcmp(command_packet,"init")==0)
		{
			initialize();
			/* Converts incoming hours to ms */
			change_water_threshold = new_water_schedule * SCHEDULE_CONVERSION_TO_MS;
			turn_on_light_threshold = new_light_on_schedule * SCHEDULE_CONVERSION_TO_MS;
			turn_off_light_threshold = new_light_off_schedule * SCHEDULE_CONVERSION_TO_MS;
			dosage = new_dosage;
			response_requested = false;
		}
		if (strcmp(command_packet, "update") == 0)
		{
			/* Converts incoming hours to ms */
			change_water_threshold = new_water_schedule * SCHEDULE_CONVERSION_TO_MS;
			turn_on_light_threshold = new_light_on_schedule * SCHEDULE_CONVERSION_TO_MS;
			turn_off_light_threshold = new_light_off_schedule * SCHEDULE_CONVERSION_TO_MS;
			dosage = new_dosage;
			response_requested = false;
		}
		if (strcmp(command_packet, "reset") == 0)
		{
			reset();
			response_requested = false;
		}
		if (strcmp(command_packet, "req") == 0)
		{
			response_requested = true;
		}
	}
}

/* Sends response packet via UDP to server. */
void send_packet()
{ 
	if (response_requested == true)
	{
		/* Printing remote server info. Based on https://github.com/vjmuzik/NativeEthernet/blob/master/examples/UDPSendReceiveString/UDPSendReceiveString.ino */
		IPAddress remote = Udp.remoteIP();
		for (int i = 0; i < 4; i++) {
			Serial.print(remote[i], DEC);
			if (i < 3) {
				Serial.print(".");
			}
		}
		Serial.print(", port ");
		Serial.println(Udp.remotePort());


		char output_string[128],test_output_string[128];
		uint32_t voltage, current, luminosity;
		float temp, humidity;
		char lightStatus[4], airPump[4], sourcePump[4], drainPump[4], nutrientsPump[4];

		memset(output_string, 0, 64);

		if (!readTempSensor(&tempSensor, &tempData)) {
			//Serial.println ("ERROR! Temp sensor could not be read.");
		}

		voltage =		ina260.readBusVoltage();
		current =		ina260.readCurrent();
		temp =			tempData.fahrenheit;
		humidity =		tempData.humidity;
		luminosity =	tsl.getLuminosity(TSL2591_FULLSPECTRUM);
		/* Populating light response*/
		if (LED_status == 1)
		{
			strcpy(lightStatus, "ON");
		}
		else if (LED_status == 0)
		{
			strcpy(lightStatus, "OFF");
		}

		/* Populating air pump response*/
		if (air_pump.motor_status == 1)
		{
			strcpy(airPump, "ON");
		}
		else if (air_pump.motor_status == 0)
		{
			strcpy(airPump, "OFF");
		}

		/* Populating source pump response*/
		if (water_pump_source.motor_status == 1)
		{
			strcpy(sourcePump, "ON");
		}
		else if (water_pump_source.motor_status == 0)
		{
			strcpy(sourcePump, "OFF");
		}

		/* Populating drain pump response*/
		if (water_pump_drain.motor_status == 1)
		{
			strcpy(drainPump, "ON");
		}
		else if (water_pump_drain.motor_status == 0)
		{
			strcpy(drainPump, "OFF");
		}

		/* Populating nutrient response*/
		if (food_pump.motor_status == 1)
		{
			strcpy(nutrientsPump, "ON");
		}
		else if (food_pump.motor_status == 0)
		{
			strcpy(nutrientsPump, "OFF");
		}
		//luminosity;temperature;humidity;voltage;amps;lightStatus;airPump;sourcePump;drainPump;nutrientsPump
		sprintf(output_string, "%lu;%.1f;%.1f;%lu;%lu;%s;%s;%s;%s;%s", luminosity,temp,humidity, voltage, current, lightStatus, airPump, sourcePump, drainPump, nutrientsPump);

		Serial.println(output_string);

#if DEBUG
		Serial.printf("\nMeasured Temp: %f\nMeasured Humidity: %f\n", tempData.fahrenheit, tempData.humidity);
		Serial.printf("Stored Temp: %f\nStored Humidity: %f\n", temp, humidity);
		Serial.printf("String buffer: %sBuffer size: %d\n", output_string,strlen(output_string));
#endif

#if ETHERNET
		strcpy(test_output_string, "42;69;30;420;49;ON;ON;ON;ON;ON");

		Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
		Udp.write(output_string);
		Udp.endPacket();
#endif
		response_requested = false;
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

void read_current()
{
	if (ina260.readCurrent() >= CURRENT_THRESHOLD)
	{
		reset();
		system_attention_flag = 1;
	}
}

/* Finds Teensy MAC address and populates local MAC address buffer (6 bytes). Sourced from:
   https://forum.pjrc.com/threads/62932-Teensy-4-1-MAC-Address
*/
void teensyMAC(uint8_t* mac) {
	for (uint8_t by = 0; by < 2; by++) mac[by] = (HW_OCOTP_MAC1 >> ((1 - by) * 8)) & 0xFF;
	for (uint8_t by = 0; by < 4; by++) mac[by + 2] = (HW_OCOTP_MAC0 >> ((3 - by) * 8)) & 0xFF;
	Serial.printf("MAC: %02x:%02x:%02x:%02x:%02x:%02x\n", mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
}

void print_ethernet_test() {
	EthernetClient client = server.available();
	if (client) {
		Serial.println("new client");
		// an http request ends with a blank line
		boolean currentLineIsBlank = true;
		while (client.connected()) {
			if (client.available()) {
				char c = client.read();
				Serial.write(c);
				// if you've gotten to the end of the line (received a newline
				// character) and the line is blank, the http request has ended,
				// so you can send a reply
				if (c == '\n' && currentLineIsBlank) {
					// send a standard http response header
					client.println("HTTP/1.1 200 OK");
					client.println("Content-Type: text/html");
					client.println("Connection: close");  // the connection will be closed after completion of the response
					client.println("Refresh: 5");  // refresh the page automatically every 5 sec
					client.println();
					client.println("<!DOCTYPE HTML>");
					client.println("<html>");
					client.println("Hello from Auto Gardener!");
					client.println("</html>");
					break;
				}
				if (c == '\n') {
					// you're starting a new line
					currentLineIsBlank = true;
				}
				else if (c != '\r') {
					// you've gotten a character on the current line
					currentLineIsBlank = false;
				}
			}
		}
		// give the web browser time to receive the data
		delay(1);
		// close the connection:
		client.stop();
		Serial.println("client disconnected");
	}
}

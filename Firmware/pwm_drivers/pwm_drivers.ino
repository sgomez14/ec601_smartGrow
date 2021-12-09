/*
 Name:		Smart_Grow.ino
 Created:	10/7/2021 7:58:56 PM
 Author:	bmk

 Notes:
 Motor & MOSFET Wiring: https://www.youtube.com/watch?v=3PkpOeHTnfo
 Air Pump: https://www.youtube.com/watch?v=nGVykVrly9g


*/

#include "pwm_functions.h"

EthernetServer server(80);

void setup() {
	Serial.begin(9600);

	
#if DEBUG
	while (!Serial) {
		; // wait for serial port to connect. Needed for native USB
	}
#endif

	if (tsl.begin())
	{
		Serial.println(F("Found a TSL2591 sensor"));
	}
	else
	{
		Serial.println(F("No sensor found ... check your wiring?"));
		while (1);
	}
	
	if (!ina260.begin()) {
		Serial.println("Couldn't find INA260 chip");
		while (1);
	}
	else
	{
		Serial.println("Found INA260 chip");
	}
	
	teensyMAC(mac);

	/* Start networking */	
#if ETHERNET
	Serial.println("Begin ethernet");
	Ethernet.begin(mac, device_ip);
	Serial.println("Begin UDP");
	Udp.begin(local_port);
	server.begin();
	Serial.print("server is at ");
	Serial.println(Ethernet.localIP());
#endif // ETHERNET

#if DEBUG
	Serial.println("Entering debug loop: ");
	/*
	PWM_calibration(&air_pump);
	PWM_calibration(&water_pump_source);
	PWM_calibration(&water_pump_drain);
	PWM_calibration(&food_pump);
	PWM_calibration(&LED);
	*/
	while (1) 
	{ 
		Serial.println("In debug loop: ");
		PWM_set_percent(&water_pump_source, 100);
		delay(30000);
		PWM_set_percent(&water_pump_source, 0);
		PWM_set_percent(&water_pump_drain, 80);
		delay(30000);
		PWM_set_percent(&water_pump_drain, 0);
		PWM_set_percent(&food_pump, 100);
		delay(2000);
		PWM_set_percent(&food_pump, 0);
	}
#endif

	Serial.println("Init temp sensor");
	tempSensorInit();

	Serial.println("Init light sensor");
	init_light_sensor();

	//initialize();

	Serial.println("Initial 2 sec delay:");
	delay(2000);



	pinMode(13, OUTPUT);
	pinMode(LED.pin, OUTPUT);
	digitalWrite(13, HIGH);
	pinMode(DHTPIN, INPUT);
}
 
// the loop function runs over and over again until power down or reset
void loop() {
	//Serial.println("Top of loop");
	//print_ethernet_test();
	if (system_attention_flag)
	{
		Serial.printf("ERROR IN SYSTEM. CURRENT OVERDRAW PROTECTION ACTIVATED. CHECK FOR PUMP JAMS.\n");
		reset();
	}
	else
	{
		/* Receive command packet*/
		get_packet();

		/* Scheduler */
		scheduler();

		/* Send response packet*/
		send_packet();

		/* Printing timers for debugging */
#if DEBUG
		Serial.print("change_water: ");
		Serial.println(change_water);
		Serial.print("turn_off_light: ");
		Serial.println(turn_off_light);
		Serial.print("turn_on_light: ");
		Serial.println(turn_on_light);
		Serial.println();
#endif

	}
	//Serial.printf("Light Status: %d\n", LED_status);
	//Serial.printf("Light ON: %u\nLight OFF: %u\n", turn_on_light_threshold, turn_off_light_threshold);
	delay(200);
}

/*
 Name:		Smart_Grow.ino
 Created:	10/7/2021 7:58:56 PM
 Author:	bmk

 Notes:
 Motor & MOSFET Wiring: https://www.youtube.com/watch?v=3PkpOeHTnfo
 Air Pump: https://www.youtube.com/watch?v=nGVykVrly9g


*/

#include "pwm_functions.h"


void setup() {
	Serial.begin(9600);
	while (!Serial) {
		; // wait for serial port to connect. Needed for native USB
	}

	pinMode(13, OUTPUT);
	pinMode(LED.pin, OUTPUT);
	digitalWrite(13, HIGH);
	pinMode(PLANTER_WATER_SENSOR_PIN, INPUT);
	pinMode(DHTPIN, INPUT);

	tempSensorInit();

	Serial.println("Initial 2 sec delay:");
	delay(2000);

	/* Resetting timers before superloop() */
	change_water = 0;
	turn_off_light = 0;
	turn_on_light = 0;

	initialize();

	//teensyMAC(mac);

#if DEBUG
	//PWM_calibration(&water_pump_source);
	//PWM_calibration(&water_pump_drain);
	//PWM_calibration(&food_pump);
	//PWM_calibration(&air_pump);
	//PWM_calibration(&LED);
#endif
}
 
// the loop function runs over and over again until power down or reset
void loop() {

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
	delay(500);
}

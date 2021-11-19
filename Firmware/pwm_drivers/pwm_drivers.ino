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

	Serial.println("Initial 2 sec delay:");
	delay(2000);

	initialize();

	/* Resetting timers before superloop() */
	change_water = 0;
	turn_off_light = 0;
	turn_on_light = 0;

#if DEBUG
	PWM_calibration(&water_pump_source);
	PWM_calibration(&water_pump_drain);
	PWM_calibration(&food_pump);
	PWM_calibration(&air_pump);
	PWM_calibration(&LED);
	Serial.print("Water Sensor: ");
	Serial.println(digitalReadFast(PLANTER_WATER_SENSOR_PIN));
	while(1){ ; }
#endif
}
 
// the loop function runs over and over again until power down or reset
void loop() {
	
	/* Receive command packet*/

	/* Scheduler */
	scheduler();

	/* Send response packet*/


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

	delay(1000);
}

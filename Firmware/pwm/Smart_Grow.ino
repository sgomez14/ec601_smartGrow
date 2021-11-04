/*
 Name:		Smart_Grow.ino
 Created:	10/7/2021 7:58:56 PM
 Author:	bmk

 Notes:
 Motor & MOSFET Wiring: https://www.youtube.com/watch?v=3PkpOeHTnfo
 Air Pump: https://www.youtube.com/watch?v=nGVykVrly9g


*/

#include "functions.h"



// the setup function runs once when you press reset or power the board

PWM_Pump pump1 = { 33, 145, 255 };
PWM_Pump pump2 = { 36, 180, 255 };
PWM_Pump LED = { 37, 145, 255 };

void setup() {
	Serial.begin(9600);
	while (!Serial) {
		; // wait for serial port to connect. Needed for native USB
	}

	pinMode(13, OUTPUT);
	pinMode(LED.pin, OUTPUT);
	digitalWrite(13, HIGH);

	delay(5000);

	//PWM_Calibration(pump2);
}

// the loop function runs over and over again until power down or reset
void loop() {
	//PWM_Calibration(LED);
	PWM_set_percent(pump2, 10);
	delay(1000);
}

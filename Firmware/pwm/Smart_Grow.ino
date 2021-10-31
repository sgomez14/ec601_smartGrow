/*
 Name:		Smart_Grow.ino
 Created:	10/7/2021 7:58:56 PM
 Author:	bmk

 Notes:
 Motor & MOSFET Wiring: https://www.youtube.com/watch?v=3PkpOeHTnfo


*/

#include "functions.h"

struct PWM_Pump {
	uint8_t pin;
	uint8_t min;
	uint8_t max;
};

// the setup function runs once when you press reset or power the board

PWM_Pump pump1 = { 33, 145, 255 };

void setup() {
	Serial.begin(9600);
	while (!Serial) {
		; // wait for serial port to connect. Needed for native USB
	}

	/* Setting up pumps */
	/*
	pump1.pin = 33;
	pump1.min = 120;
	pump1.max = 255;
	*/

	pinMode(13, OUTPUT);
	pinMode(pump1.pin, OUTPUT);
	digitalWrite(13, HIGH);

	delay(5000);
}

// the loop function runs over and over again until power down or reset
void loop() {
	PWM_Calibration(pump1.pin, pump1.min, pump1.max);
	/*
	Serial.println("HIGH");
	digitalWrite(PWM_Pump, HIGH);

	delay(1000);

	Serial.println("LOW");
	digitalWrite(PWM_Pump, LOW);

	delay(1000);
	*/
}

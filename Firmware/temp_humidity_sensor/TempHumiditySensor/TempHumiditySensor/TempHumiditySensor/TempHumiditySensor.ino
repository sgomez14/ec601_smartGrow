/*
 Name:		TempHumiditySensor.ino
 Created:	10/22/2021 12:48:59 PM
 Author:	santi09
*/

#include "tempSensor.h"

// the setup function runs once when you press reset or power the board
void setup() {
	Serial.begin(9600);

	Serial.println("Firmware for TempHumiditySensor!");

	// Initialize sensor
	tempSensorInit();

	while (!Serial) {
		; // wait for serial port to connect. Needed for native USB
	}
}

// the loop function runs over and over again until power down or reset
void loop() {
	// Wait a few seconds between measurements:
	delay(2000);

	//tempSensor is the sensor object and
	//tempData is the data structure for storing the sensor data

	if (readTempSensor(&tempSensor,&tempData))
	{
		printTempData(&tempData);
	}
	else
	{
		Serial.println("Failed to read from DHT sensor!");
	}
}

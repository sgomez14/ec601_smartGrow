
/* 
	 Name:		tempSensor.h
	 Created:	10/22/2021 12:48:59 PM
	 Author:	Santiago Gomez, santi09@bu.edu
	
	Temp/Humidity Sensor Firmware Adapted from Tutorial Below
 
	Arduino example code for DHT11, DHT22/AM2302 and DHT21/AM2301 temperature and humidity sensors.
	More info: www.www.makerguides.com/dht11-dht22-arduino-tutorial
*/

#ifndef _TEST_TEMPSENSOR_h
#define _TEST_TEMPSENSOR_h

#if defined(ARDUINO) && ARDUINO >= 100
#include "arduino.h"
#else
#include "WProgram.h"
#endif
#include <Adafruit_Sensor.h>
#include <DHT.h>

// Set DHT digital pin for Teensy 4.1:
#define DHTPIN 32

// Set DHT type
#define DHTTYPE DHT22   // DHT 22  (AM2302)

typedef struct tempSensorData {
	float humidity;
	float fahrenheit;
	float celcius;
	float heatIndex_F;
	float heatIndex_C;
}tempSensorData;

extern DHT tempSensor; // = DHT(DHTPIN, DHTTYPE);

extern tempSensorData tempData;

//wrapper function that reads humidity, temp, and heat index
extern bool readTempSensor(DHT* dhtSensor, tempSensorData* tempData);

extern void printTempData(tempSensorData* tempData);

extern void tempSensorInit(void);



#endif



/*
     Name:		tempSensor.cpp
     Created:	10/22/2021 12:48:59 PM
     Author:	Santiago Gomez, santi09@bu.edu

    Temp/Humidity Sensor Firmware Adapted from Tutorial Below

    Arduino example code for DHT11, DHT22/AM2302 and DHT21/AM2301 temperature and humidity sensors.
    More info: www.www.makerguides.com/dht11-dht22-arduino-tutorial
*/

#include "tempSensor.h"

// Initialize DHT sensor for normal 16mhz Arduino:
DHT tempSensor = DHT(DHTPIN, DHTTYPE);

// Initialize temperature data structure
tempSensorData tempData = { 0,0,0,0,0 };

// Wrapper function that reads humidity, temp, and heat index
// returns bool indicating if reading the sensor was successful
// pass in pointers to sensor object and sensor data structure
bool readTempSensor(DHT* dhtSensor, tempSensorData* tempData)
{
    // Reading temperature or humidity takes about 250 milliseconds!
    // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)

    // Read the humidity in %:
    tempData->humidity = dhtSensor->readHumidity();

    // Read the temperature as Celsius:
    tempData->celcius = dhtSensor->readTemperature();

    // Read the temperature as Fahrenheit:
    tempData->fahrenheit = dhtSensor->readTemperature(true);

    // Check if any reads failed and exit early (to try again):
    if (isnan(tempData->humidity) || isnan(tempData->celcius) || isnan(tempData->fahrenheit)) {

        //reset tempData values
        tempData->humidity = 0;
        tempData->fahrenheit = 0;
        tempData->celcius = 0;
        tempData->heatIndex_F = 0;
        tempData->heatIndex_C = 0;
        return false;
    }

    // Compute heat index in Fahrenheit (default):
    tempData->heatIndex_F = dhtSensor->computeHeatIndex(tempData->fahrenheit, tempData->humidity);

    // Compute heat index in Celsius:
    tempData->heatIndex_C = dhtSensor->computeHeatIndex(tempData->celcius, tempData->humidity, false);

    return true;
}

// Function for printing sensor data
void printTempData(tempSensorData* tempData)
{
    Serial.print("Humidity: ");
    Serial.print(tempData->humidity);
    Serial.print(" % ");
    Serial.print("Temperature: ");
    Serial.print(tempData->celcius);
    Serial.print(" \xC2\xB0");
    Serial.print("C | ");
    Serial.print(tempData->fahrenheit);
    Serial.print(" \xC2\xB0");
    Serial.print("F ");
    Serial.print("Heat index: ");
    Serial.print(tempData->heatIndex_C);
    Serial.print(" \xC2\xB0");
    Serial.print("C | ");
    Serial.print(tempData->heatIndex_F);
    Serial.print(" \xC2\xB0");
    Serial.println("F");
}

void tempSensorInit(void)
{
    // Initialize sensor
    tempSensor.begin();
}
/*
 Name:    Light_sensor.ino
 Author:  Yuan
 Notes:
 TSL2591 example code form https://learn.adafruit.com/adafruit-tsl2591/wiring-and-test
*/

#include "lightfunction.h"


Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591);

void setup(void) 
{
  Serial.begin(9600);
  if (tsl.begin()) 
  {
    Serial.println(F("Found a TSL2591 sensor"));
  } 
  else 
  {
    Serial.println(F("No sensor found ... check your wiring?"));
    while (1);
  }
  /* Configure the sensor */
  configureSensor();

}

void loop(void) 
{  
  advancedRead();
  delay(500);
}

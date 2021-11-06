/*
 Name:    Light_sensor.ino
 Author:  Yuan
 Notes:
 TSL2591 example code form https://learn.adafruit.com/adafruit-tsl2591/wiring-and-test
*/

#include "lightsensor.h"


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
  /* Initial the sensor */
  
  init_light_sensor();
  light_sensor_init_info();

}

void loop(void) 
{  
  print_light_data();
  delay(500);
}

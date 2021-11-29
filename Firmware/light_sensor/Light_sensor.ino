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
  /* Initial the sensor */
  
  init_light_sensor();
  light_sensor_init_info();

}

void loop(void) 
{  
  if(read_light_data()){
    print_light_data();
    delay(500);
  }
  else{
    Serial.println(F("Wrong light data"));
  }

}

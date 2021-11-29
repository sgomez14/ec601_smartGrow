//lightsensor.h

#ifndef _LIGHT_SENSOR_h
#define _LIGHT_SENSOR_h

#if defined(ARDUINO) && ARDUINO >= 100
#include "arduino.h"
#else
#include "WProgram.h"
#endif

#include "Wire.h"
#include "Adafruit_Sensor.h"
#include "Adafruit_TSL2591.h"

//This is our light sensor object
extern Adafruit_TSL2591 tsl;

extern uint32_t lum;
extern uint16_t ir;
extern uint16_t full;
extern uint16_t lux;

extern void light_sensor_init_info(void);
extern void print_light_data(void);
extern void init_light_sensor(void);
extern bool read_light_data(void);

#endif

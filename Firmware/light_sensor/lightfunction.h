//lightfunction.h

#ifndef _LIGHT_FUNC_h
#define _LIGHT_FUNC_h

#if defined(ARDUINO) && ARDUINO >= 100
#include "arduino.h"
#else
#include "WProgram.h"
#endif

#include "Wire.h"
#include "Adafruit_Sensor.h"
#include "Adafruit_TSL2591.h"




void configureSensor(void);
void advancedRead(void);

#endif

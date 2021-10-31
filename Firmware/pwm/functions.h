// functions.h

#ifndef _FUNCTIONS_h
#define _FUNCTIONS_h

#if defined(ARDUINO) && ARDUINO >= 100
	#include "arduino.h"
#else
	#include "WProgram.h"
#endif
void PWM_Calibration(uint8_t gpio_pin, uint8_t min, uint8_t max);

#endif


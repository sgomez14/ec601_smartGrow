// functions.h

#ifndef _FUNCTIONS_h
#define _FUNCTIONS_h

#if defined(ARDUINO) && ARDUINO >= 100
	#include "arduino.h"
#else
	#include "WProgram.h"
#endif



struct PWM_Pump {
	uint8_t pin;
	uint8_t min;
	uint8_t max;
};

void PWM_Calibration(PWM_Pump *pwm_pump);
void PWM_set_percent(PWM_Pump *pwm_pump, uint8_t percent);
void Dose_food(PWM_Pump* pwm_pump, uint8_t ml);
 
extern PWM_Pump pump1 = { 33, 145, 255 };
extern PWM_Pump pump2 = { 36, 180, 255 };
extern PWM_Pump air_pump = { 23, 50, 200 };
extern PWM_Pump LED = { 37, 145, 255 };

extern String command_packet;

#endif


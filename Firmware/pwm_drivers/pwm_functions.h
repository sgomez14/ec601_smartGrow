// functions.h

#ifndef _FUNCTIONS_h
#define _FUNCTIONS_h

#if defined(ARDUINO) && ARDUINO >= 100
	#include "arduino.h"
#else
	#include "WProgram.h"
#endif

/* ml per sec, measured by running how long it takes to fill 100 ml. */
#define FILL_RATE 10 

typedef struct PWM_device {
	uint8_t pin;
	uint8_t min;
	uint8_t max;
}PWM_device;

extern PWM_device water_pump1;
extern PWM_device water_pump2;
extern PWM_device food_pump;
extern PWM_device air_pump;
extern PWM_device LED;
extern String command_packet;

extern void PWM_calibration(PWM_device *pwm_device);
extern void PWM_set_percent(PWM_device *pwm_device, uint8_t percent);
extern void dose_food(PWM_device *pwm_device, uint8_t ml);


#endif


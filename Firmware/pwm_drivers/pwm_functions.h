// functions.h

#ifndef _PWM_FUNCTIONS_h
#define _PWM_FUNCTIONS_h

#if defined(ARDUINO) && ARDUINO >= 100
	#include "arduino.h"
#else
	#include "WProgram.h"
#endif

#endif

/* ml per sec, measured by running how long it takes to fill 100 ml. */
#define FILL_RATE 10 
#define PLANTER_WATER_SENSOR_PIN 23
#define DEBUG 0

typedef struct PWM_device {
	uint8_t pin;
	uint8_t min;
	uint8_t max;
}PWM_device;


extern PWM_device water_pump_source;
extern PWM_device water_pump_drain;
extern PWM_device food_pump;
extern PWM_device air_pump;
extern PWM_device LED;
extern String command_packet;


/* Various timer variables for scheduling functions. Can go up to ~40 days. */
/* Device Timers, for manually controlling devices.*/
extern elapsedMillis change_water;
extern elapsedMillis turn_on_light;
extern elapsedMillis turn_off_light;


/* Global variables for communicating between select functions. */

extern unsigned int change_water_threshold, turn_on_light_threshold, turn_off_light_threshold;

extern bool LED_status, tank_is_full_flag; /* 1 := on, 0 := off */
extern unsigned long time_to_fill;

extern void PWM_calibration(PWM_device *pwm_device);
extern void PWM_set_percent(PWM_device *pwm_device, uint8_t percent);
extern void dose_food(PWM_device *pwm_device, uint8_t ml);
extern void fill_tank(PWM_device* pwm_device);
extern void empty_tank(PWM_device* pwm_device);
void toggle_light(PWM_device* pwm_device);
void reset();
void initialize();
void scheduler();
void get_packet();
void send_packet();

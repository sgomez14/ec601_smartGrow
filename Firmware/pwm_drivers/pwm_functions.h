// functions.h

#ifndef _PWM_FUNCTIONS_h
#define _PWM_FUNCTIONS_h

#if defined(ARDUINO) && ARDUINO >= 100
	#include "arduino.h"
#else
	#include "WProgram.h"
#endif

#endif


#include <SPI.h>
#include <Adafruit_INA260.h>
#include <DHT_U.h>
#include <DHT.h>
#include <NativeEthernet.h>
#include <NativeEthernetUdp.h>
#include "lightsensor.h"
#include "temp_sensor.h"
#include <string.h>

/* ml per sec, measured by running how long it takes to fill 100 ml. */
#define FILL_RATE 10 
#define PLANTER_WATER_SENSOR_PIN 24
#define DEBUG 1
#define ETHERNET 0

typedef struct PWM_device {
	uint8_t pin;
	uint8_t min;
	uint8_t max;
} PWM_device;

typedef struct power_consumption
{
	float source_current;
	float drain_current;
	float food_current;
	float light_current;
} power_consumption;

extern power_consumption system_device_health;
extern PWM_device water_pump_source;
extern PWM_device water_pump_drain;
extern PWM_device food_pump;
extern PWM_device air_pump;
extern PWM_device LED;
extern String command_packet;
extern DHT tempSensor;


/* Various timer variables for scheduling functions. Can go up to ~40 days. */
/* Device Timers, for manually controlling devices.*/
extern elapsedMillis change_water;
extern elapsedMillis turn_on_light;
extern elapsedMillis turn_off_light;

/* Networking Variables */
extern byte mac[6];
extern int local_port;
/*
extern const int input_packet_size;
extern byte input_packet_buffer[];
extern const int output_packet_size;
extern byte output_packet_buffer[];
*/
extern IPAddress server_IP;
extern IPAddress device_ip;
extern int server_port;

/* Global variables for communicating between select functions. */

extern Adafruit_INA260 ina260;
extern unsigned int change_water_threshold, turn_on_light_threshold, turn_off_light_threshold;

extern bool LED_status, tank_is_full_flag; /* 1 := on, 0 := off */
extern unsigned long time_to_fill;
extern bool response_requested;
extern uint8_t dosage;

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
void calibrate_power_draw();
void teensyMAC(uint8_t* mac);
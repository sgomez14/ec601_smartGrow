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
#define DEBUG 0
#define ETHERNET 1
#define CURRENT_THRESHOLD 7000
#define SCHEDULE_CONVERSION_TO_MS 1000

typedef struct PWM_device {
	uint8_t pin;
	uint8_t min;
	uint8_t max;
  uint8_t motor_status;
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
extern EthernetUDP Udp;
extern EthernetServer server;
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
extern bool system_attention_flag; /* At the start of each loop, the current draw is measured. If above a threshold, all motors turn off an an ERROR alert is sent to. Operation of the system pauses until checked. Air pump remains on, as its current source is different from the DC motors. */
extern uint8_t dosage;

extern void PWM_calibration(PWM_device *pwm_device);
extern void PWM_set_percent(PWM_device *pwm_device, uint8_t percent);
extern void dose_food(PWM_device *pwm_device, uint8_t ml);
extern void fill_tank(PWM_device* pwm_device);
extern void empty_tank(PWM_device* pwm_device);
extern void toggle_light(PWM_device* pwm_device);
extern void reset();
extern void initialize();
extern void scheduler();
extern void get_packet();
extern void send_packet();
extern void calibrate_power_draw();
extern void read_current();
extern void teensyMAC(uint8_t* mac);
extern void print_ethernet_test();

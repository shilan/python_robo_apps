# -*- coding: UTF-8 -*-
## https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print ("Distance Measurement in Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Ensure that the Trigger pin is set low, and give the sensor a second to settle.
GPIO.output(TRIG, False)
print ("Wait for sensor to settle")
time.sleep(2)

# The HC-SR04 sensor requires a short 10uS pulse to trigger the module.
# (8 ultrasound bursts at 40 kHz)
# To create our trigger pulse, we set out trigger pin high for 10uS then set it low again.
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)


# We have sent our pulse signal we need to listen to our input pin
# Timestamp of when the latest time pin was low
while GPIO.input(ECHO) == 0:
    pulse_start = time.time()
    
while GPIO.input(ECHO) == 1:
    pulse_end = time.time()
    
pulse_duration = pulse_end - pulse_start

# Speed = Distance / Time
# Speed of sound at sea level: 343m/s, should be devided to 2 for going and returning
distance = pulse_duration * 17150
distance = round(distance, 2)

print ("Distance: ",distance,"cm")

# Remember to clean
GPIO.cleanup()




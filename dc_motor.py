# -*- coding: UTF-8 -*-
## https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1_Input =  16    # Input Pin
Motor2_Input =  19    # Input Pin
Motor3_Enable = 25

GPIO.setup(Motor1_Input, GPIO.OUT)
GPIO.setup(Motor2_Input, GPIO.OUT)
GPIO.setup(Motor3_Enable, GPIO.OUT)

# Forward
print("forward")
pwm = GPIO.PWM(Motor3_Enable, 100)
pwm.start(0)

GPIO.output(Motor1_Input, GPIO.HIGH)
GPIO.output(Motor2_Input, GPIO.LOW)

pwm.ChangeDutyCycle(25)
GPIO.output(Motor3_Enable, GPIO.HIGH)
sleep(3)

GPIO.output(Motor3_Enable, GPIO.LOW)

# Backward
print("backward")
GPIO.output(Motor1_Input, GPIO.LOW)
GPIO.output(Motor2_Input, GPIO.HIGH)

pwm.ChangeDutyCycle(75)
GPIO.output(Motor3_Enable, GPIO.HIGH)
sleep(3)

GPIO.output(Motor3_Enable, GPIO.LOW)

print("stop")
pwm.stop()



GPIO.cleanup()
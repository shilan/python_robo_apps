# -*- coding: UTF-8 -*-

# import libraries
import RPi.GPIO as GPIO
import time

# set GPIO numbering
GPIO.setmode(GPIO.BOARD)

# set pin as output, set servo1 as pin 11 as PWM
GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50) # pin 11 -> 50Hz pulse

# start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print("Wait for 2 seconds")
time.sleep(2)

# move the servo
print("Rotate 180 degrees in 10 steps!")

# define variable duty
duty = 2

# Loop from 2 to 12 (0 to 180 degrees) basically 10 steps
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.1)
    servo1.ChangeDutyCycle(0) # to optimize the movement of servo, we set the motor to pulse off (no move)
    time.sleep(0.7)
    duty += 1

# wait few seconds
time.sleep(2)

# turn back to 90 degrees
servo1.ChangeDutyCycle(7)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
time.sleep(1.5)

# turn back to 0 degree
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)


# Clean things up
servo1.stop()
GPIO.cleanup()
print("Goodbye!")
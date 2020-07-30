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

try:
    # Loop forever to get input from the user, ctrl + c to stop
    while True:
        angle = float(input("enter a degree value between 0 to 180:"))        
        servo1.ChangeDutyCycle(2 + (angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0) # to optimize the movement of servo (avoid jitter), we set the motor to pulse off (stop)
          

    # wait few seconds
    time.sleep(2)

# Clean things up, always even ctrl+c cannot skip this part of the code
finally:
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye!")

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

# set pin as output, set servo1 as pin 11 as PWM
SERVO_PWM = 17
GPIO.setup(SERVO_PWM, GPIO.OUT)
servo1 = GPIO.PWM(SERVO_PWM, 50) # pin 11 -> 50Hz pulse


def distance():
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


    # We’ve sent our pulse signal we need to listen to our input pin
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
    return distance

def motor():
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



if __name__ == '__main__':
    # Stop with ctrl + c
    try:
        while True:
            dist = distance()
            print ("Distance: ",dist,"cm")
            if dist > 100:
                motor()
            
    except KeyboardInterrupt:
        print("Measurement stopped by user")
        # Remember to clean
        GPIO.cleanup()
        servo1.stop()
        






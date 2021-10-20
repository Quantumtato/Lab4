#!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import time
import json

ledPin1 = 19
ledPin2 = 20
ledPin3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

pwm1 = GPIO.PWM(ledPin1, 100) # PWM object on our pin at 100 Hz
pwm2 = GPIO.PWM(ledPin2, 100)
pwm3 = GPIO.PWM(ledPin3, 100)
pwm.start(0) # start with LED off

while True:
  with open("led_pwm.txt", 'r') as f:
    data = json.load(f)
    dutyCycle = float(data['slider1']) # read duty cycle value from file
    option = int(data['option'])
  if option == 1:
    pwm1.ChangeDutyCycle(dutyCycle)
  elif option == 2:
    pwm2.ChangeDutyCycle(dutyCycle)
  elif option == 3:
    pwm3.ChangeDutyCycle(dutyCycle)
  time.sleep(0.01)
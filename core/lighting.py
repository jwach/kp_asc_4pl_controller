from time import sleep

import RPi.GPIO as GPIO

constant_lights = set()


def wave(pins):
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
        sleep(0.05)
        GPIO.output(pin, GPIO.LOW)


def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    constant_lights.add(pin)


def off(pin):
    GPIO.output(pin, GPIO.LOW)
    constant_lights.discard(pin)


def destroy():
    print "Destroying lighting..."
    for pin in constant_lights:
        GPIO.output(pin, GPIO.LOW)
    print "Lighting destroyed."

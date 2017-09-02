from time import sleep

import RPi.GPIO as GPIO
import collections

constant_lights = set()


def startup(pins):
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)


def wave(pins):
    for i in range(3):
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
            sleep(0.05)
            GPIO.output(pin, GPIO.LOW)


def on(pins):
    GPIO.output(pins, GPIO.HIGH)
    if isinstance(pins, collections.Iterable):
        constant_lights.update(pins)
    else:
        constant_lights.add(pins)


def off(pins):
    GPIO.output(pins, GPIO.LOW)
    if isinstance(pins, collections.Iterable):
        constant_lights.difference_update(pins)
    else:
        constant_lights.remove(pins)


def destroy():
    print 'Destroying lighting...'
    for pin in constant_lights:
        GPIO.output(pin, GPIO.LOW)
    print 'Lighting destroyed.'

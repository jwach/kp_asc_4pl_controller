import os
from time import sleep

import RPi.GPIO as GPIO

from core import routines, display, lighting
from core.config import *


def bank_up_press(channel):
    display.show('BANK_UP')


def bank_down_press(channel):
    display.show('BANK_DOWN')


def preset_a_press(channel):
    display.show('PRESET A')
    lighting.on(PRESET_A_LED)  # lock here?
    lighting.off(PRESET_B_LED)
    lighting.off(PRESET_C_LED)


def preset_b_press(channel):
    display.show('PRESET B')
    lighting.off(PRESET_A_LED)  # lock here?
    lighting.on(PRESET_B_LED)
    lighting.off(PRESET_C_LED)


def preset_c_press(channel):
    display.show('PRESET C')
    lighting.off(PRESET_A_LED)  # lock here?
    lighting.off(PRESET_B_LED)
    lighting.on(PRESET_C_LED)


if not os.getuid() == 0:
    print("need root")
    exit(0)

print "KP ASC-4PL v1.0"

routines.startup()

lighting.wave((PRESET_C_LED, PRESET_B_LED, PRESET_A_LED, LOOP_1, LOOP_2, LOOP_3, LOOP_4, KILL_DRY))

GPIO.add_event_detect(BANK_UP, GPIO.FALLING, callback=bank_up_press, bouncetime=300)
GPIO.add_event_detect(BANK_DOWN, GPIO.FALLING, callback=bank_down_press, bouncetime=300)
GPIO.add_event_detect(PRESET_A, GPIO.FALLING, callback=preset_a_press, bouncetime=300)
GPIO.add_event_detect(PRESET_B, GPIO.FALLING, callback=preset_b_press, bouncetime=300)
GPIO.add_event_detect(PRESET_C, GPIO.FALLING, callback=preset_c_press, bouncetime=300)

display.show('ASC-4PL')

sleep(10)

routines.shutdown()

import os
from time import sleep

import RPi.GPIO as GPIO

from core import routines, display, lighting, banks
from core.config import *


def bank_up_press(channel):
    bank_controller.up()


def bank_down_press(channel):
    bank_controller.down()


def preset_a_press(channel):
    bank_controller.load_preset_a()


def preset_b_press(channel):
    bank_controller.load_preset_b()


def preset_c_press(channel):
    bank_controller.load_preset_c()


if not os.getuid() == 0:
    print 'need root'
    exit(0)

print 'KP ASC-4PL v1.0'

routines.startup()
bank_repository = banks.BankRepository('/mnt/data/banks.pkl')
bank_controller = banks.BankController(bank_repository)

lighting.wave((PRESET_A_LED, PRESET_B_LED, PRESET_C_LED))

display.show('ASC-4PL')

sleep(2)

bank_controller.start()

GPIO.add_event_detect(BANK_UP, GPIO.FALLING, callback=bank_up_press, bouncetime=250)
GPIO.add_event_detect(BANK_DOWN, GPIO.FALLING, callback=bank_down_press, bouncetime=250)
GPIO.add_event_detect(PRESET_A, GPIO.FALLING, callback=preset_a_press, bouncetime=300)
GPIO.add_event_detect(PRESET_B, GPIO.FALLING, callback=preset_b_press, bouncetime=300)
GPIO.add_event_detect(PRESET_C, GPIO.FALLING, callback=preset_c_press, bouncetime=300)

# we are ready
while 1:
    print 'Main loop. Idling...'
    sleep(300)

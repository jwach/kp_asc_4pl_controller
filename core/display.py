from time import sleep

import RPi.GPIO as GPIO
from threading import RLock

from core.config import *

lock = RLock()


def startup():
    with lock:
        GPIO.output(DISP_CS, GPIO.HIGH)
        GPIO.output(DISP_CLR, GPIO.HIGH)
        GPIO.output(DISP_WR, GPIO.HIGH)
        clear()


def clear():
    with lock:
        GPIO.output(DISP_CLR, GPIO.LOW)
        _default_sleep()
        GPIO.output(DISP_CLR, GPIO.HIGH)
        _default_sleep()


def show(string):
    clear()
    _write(' ')
    clear()
    _write(string)


def _default_sleep():
    sleep(0.000001)


def _write_char(bit_array):
    GPIO.output([DISP_D0, DISP_D1, DISP_D2, DISP_D3, DISP_D4, DISP_D5], bit_array)
    GPIO.output(DISP_WR, GPIO.LOW)
    _default_sleep()
    GPIO.output(DISP_WR, GPIO.HIGH)
    _default_sleep()


def _encode_char(c):
    if 64 <= ord(c) <= 95:
        return ord(c) - 64
    elif 32 <= ord(c) <= 63:
        return ord(c)
    else:
        raise Exception('Invalid character')


def _write(string):
    with lock:
        for c in string:
            byte = _encode_char(c)
            bit_array = []
            for i in range(6):
                bit_array.append((1 << i) & byte)
            _write_char(bit_array)

import os
from time import sleep

import RPi.GPIO as GPIO

from core import routines
from core.config import *


# def write():
#     GPIO.output(DISP_D0, GPIO.HIGH)
#     GPIO.output(DISP_D1, GPIO.LOW)
#     GPIO.output(DISP_D2, GPIO.LOW)
#     GPIO.output(DISP_D3, GPIO.LOW)
#     GPIO.output(DISP_D4, GPIO.LOW)
#     GPIO.output(DISP_D5, GPIO.LOW)
#
#     GPIO.output(DISP_WR, GPIO.LOW)
#     sleep(0.000001)
#     GPIO.output(DISP_WR, GPIO.HIGH)

def encode_char(c):
    if 64 <= ord(c) <= 95:
        return ord(c) - 64
    elif 32 <= ord(c) <= 63:
        return ord(c)
    else:
        raise Exception('Invalid character')


def encode(string):
    for c in string:
        byte = encode_char(c)
        bit_array = []
        for i in range(6):
            bit_array.append((1 << i) & byte)
        write(bit_array)


def write(bit_array):
    GPIO.output([DISP_D0, DISP_D1, DISP_D2, DISP_D3, DISP_D4, DISP_D5], bit_array)
    GPIO.output(DISP_WR, GPIO.LOW)
    sleep(0.000001)
    GPIO.output(DISP_WR, GPIO.HIGH)


if not os.getuid() == 0:
    print("need root")
    exit(0)

print "KP ASC-4PL v1.0"

routines.startup()

GPIO.output(DISP_CS, GPIO.HIGH)
GPIO.output(DISP_CLR, GPIO.HIGH)
GPIO.output(DISP_WR, GPIO.HIGH)

sleep(0.1)

GPIO.output(DISP_CLR, GPIO.LOW)
sleep(0.1)
GPIO.output(DISP_CLR, GPIO.HIGH)

sleep(0.1)

for i in range(100):
    s = ''
    for y in range(i % 5):
        s += ' '
    encode(s + 'B==>')
    sleep(0.5)
    GPIO.output(DISP_CLR, GPIO.LOW)
    sleep(0.01)
    GPIO.output(DISP_CLR, GPIO.HIGH)

# routines.shutdown()

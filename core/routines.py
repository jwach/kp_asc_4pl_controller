from core.config import *
import RPi.GPIO as GPIO


def startup():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(DISP_D0, GPIO.OUT)
    GPIO.setup(DISP_D1, GPIO.OUT)
    GPIO.setup(DISP_D2, GPIO.OUT)
    GPIO.setup(DISP_D3, GPIO.OUT)
    GPIO.setup(DISP_D4, GPIO.OUT)
    GPIO.setup(DISP_D5, GPIO.OUT)

    GPIO.setup(DISP_CS, GPIO.OUT)
    GPIO.setup(DISP_WR, GPIO.OUT)
    GPIO.setup(DISP_CLR, GPIO.OUT)


def shutdown():
    GPIO.cleanup()

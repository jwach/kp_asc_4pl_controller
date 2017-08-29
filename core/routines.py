from core import display, lighting
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

    GPIO.setup(BANK_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BANK_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(KILL_DRY, GPIO.OUT)
    GPIO.setup(LOOP_1, GPIO.OUT)
    GPIO.setup(LOOP_2, GPIO.OUT)
    GPIO.setup(LOOP_3, GPIO.OUT)
    GPIO.setup(LOOP_4, GPIO.OUT)

    GPIO.setup(PRESET_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PRESET_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PRESET_C, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(PRESET_A_LED, GPIO.OUT)
    GPIO.setup(PRESET_B_LED, GPIO.OUT)
    GPIO.setup(PRESET_C_LED, GPIO.OUT)

    display.startup()


def shutdown():
    lighting.destroy()
    display.clear()
    # GPIO.cleanup()  # is it safe for all pins? maybe clear display first?

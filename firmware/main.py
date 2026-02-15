#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

from config import *
from adc_driver import init_adc, read_adc, close_adc
from motor_control import motor_init, motor_start, motor_stop
from lcd_driver import lcd_init, lcd_string


def gpio_init():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # LCD Pins
    lcd_pins = [LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7]
    for pin in lcd_pins:
        GPIO.setup(pin, GPIO.OUT)

    # Buttons
    input_pins = [WAFER_BTN, COUNT_BTN, RESET_BTN, STOP_BTN]
    for pin in input_pins:
        GPIO.setup(pin, GPIO.IN)

    motor_init()


def main():

    gpio_init()
    init_adc()
    lcd_init()

    lcd_string("Wafer Align Sys", LCD_LINE_1)
    lcd_string("Initializing...", LCD_LINE_2)
    time.sleep(2)

    wafer_count = 0
    count_prev = False
    reset_prev = False

    while True:

        if GPIO.input(STOP_BTN):
            motor_stop()
            lcd_string("EMERGENCY STOP", LCD_LINE_1)
            lcd_string("System Halted", LCD_LINE_2)
            time.sleep(1)
            continue

        if GPIO.input(WAFER_BTN):

            light = read_adc(LDR_CHANNEL)

            if light < ALIGN_THRESHOLD:
                lcd_string("Aligning...", LCD_LINE_1)
                lcd_string("Motor: ON", LCD_LINE_2)
                motor_start()
            else:
                lcd_string("Wafer Aligned", LCD_LINE_1)
                lcd_string("Motor: OFF", LCD_LINE_2)
                motor_stop()

            # Count Logic
            if GPIO.input(COUNT_BTN) and not count_prev:
                if wafer_count < MAX_WAFER_COUNT:
                    wafer_count += 1
                    lcd_string(f"Count: {wafer_count:02}", LCD_LINE_1)
                    lcd_string("Added Wafer", LCD_LINE_2)
                count_prev = True
                time.sleep(0.3)
            elif not GPIO.input(COUNT_BTN):
                count_prev = False

            # Reset Logic
            if GPIO.input(RESET_BTN) and not reset_prev:
                wafer_count = 0
                lcd_string("Count Reset", LCD_LINE_1)
                lcd_string("Count: 00", LCD_LINE_2)
                reset_prev = True
                time.sleep(0.3)
            elif not GPIO.input(RESET_BTN):
                reset_prev = False

        else:
            motor_stop()
            lcd_string("Wafer Missing", LCD_LINE_1)
            lcd_string("Insert Wafer", LCD_LINE_2)
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        close_adc()


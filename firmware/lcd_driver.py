import RPi.GPIO as GPIO
import time
from config import *

def lcd_init():
    lcd_byte(0x33, False)
    lcd_byte(0x32, False)
    lcd_byte(0x06, False)
    lcd_byte(0x0C, False)
    lcd_byte(0x28, False)
    lcd_byte(0x01, False)
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    GPIO.output(LCD_RS, mode)

    GPIO.output(LCD_D4, bool(bits & 0x10))
    GPIO.output(LCD_D5, bool(bits & 0x20))
    GPIO.output(LCD_D6, bool(bits & 0x40))
    GPIO.output(LCD_D7, bool(bits & 0x80))
    lcd_toggle_enable()

    GPIO.output(LCD_D4, bool(bits & 0x01))
    GPIO.output(LCD_D5, bool(bits & 0x02))
    GPIO.output(LCD_D6, bool(bits & 0x04))
    GPIO.output(LCD_D7, bool(bits & 0x08))
    lcd_toggle_enable()

def lcd_toggle_enable():
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)

def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, False)
    for char in message:
        lcd_byte(ord(char), True)

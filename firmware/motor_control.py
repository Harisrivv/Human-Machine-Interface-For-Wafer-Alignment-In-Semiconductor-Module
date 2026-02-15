import RPi.GPIO as GPIO
from config import MOTOR_IN1, MOTOR_IN2, RED_LED, GREEN_LED

def motor_init():
    GPIO.setup(MOTOR_IN1, GPIO.OUT)
    GPIO.setup(MOTOR_IN2, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.setup(GREEN_LED, GPIO.OUT)

def motor_start():
    GPIO.output(MOTOR_IN1, True)
    GPIO.output(MOTOR_IN2, False)
    GPIO.output(RED_LED, True)
    GPIO.output(GREEN_LED, False)

def motor_stop():
    GPIO.output(MOTOR_IN1, False)
    GPIO.output(MOTOR_IN2, False)
    GPIO.output(RED_LED, False)
    GPIO.output(GREEN_LED, True)


import time
from config import gpio_green, gpio_yellow, gpio_red, use_fake_traffic_light

if not use_fake_traffic_light:
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_green, GPIO.OUT)
    GPIO.setup(gpio_yellow, GPIO.OUT)
    GPIO.setup(gpio_red, GPIO.OUT)

    on = GPIO.HIGH
    off = GPIO.LOW
    green = gpio_green
    yellow = gpio_yellow
    red = gpio_red


class TrafficLight:

    def display_green(self):
        set_traffic_light(on, off, off)

    def display_yellow(self):
        set_traffic_light(off, on, off)

    def display_red(self):
        set_traffic_light(off, off, on)

    def display_error(self):
        flash(5, set_traffic_light(on, on, on))
        set_traffic_light(off, off, off)


def flash(times: int, fn):
    for x in range(times):
        fn()
        time.sleep(1)
        set_traffic_light(off, off, off)
        time.sleep(1)


def set_traffic_light(green, yellow, red):
    GPIO.output(gpio_red, green)
    GPIO.output(gpio_yellow, yellow)
    GPIO.output(gpio_green, red)

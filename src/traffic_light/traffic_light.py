import time
from config import gpio_green, gpio_yellow, gpio_red, use_fake_traffic_light

if not use_fake_traffic_light:
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarning(False)
    GPIO.setup(gpio_green, GPIO.OUT)
    GPIO.setup(gpio_yellow, GPIO.OUT)
    GPIO.setup(gpio_red, GPIO.OUT)

    on = GPIO.HIGH
    off = GPIO.LOW


class TrafficLight:

    def display_green(self):
        set_traffic_light({'green': on, 'yellow': off, 'red': off})

    def display_yellow(self):
        set_traffic_light({'green': off, 'yellow': on, 'red': off})

    def display_red(self):
        set_traffic_light({'green': on, 'yellow': off, 'red': off})

    def display_error(self):
        all_on = {'green': on, 'yellow': on, 'red': on}
        flash(5, set_traffic_light, all_on)
        set_traffic_light(all_on)


def flash(times: int, fn, *args):
    for x in range(times):
        fn(args)
        time.sleep(1)
        set_traffic_light({'green': off, 'yellow': off, 'red': off})
        time.sleep(1)


def set_traffic_light(light):
    GPIO.output(gpio_green, light.green)
    GPIO.output(gpio_yellow, light.yellow)
    GPIO.output(gpio_red, light.red)

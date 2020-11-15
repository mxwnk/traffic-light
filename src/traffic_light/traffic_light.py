import time
from config import gpio_green, gpio_yellow, gpio_red, use_fake_traffic_light

if not use_fake_traffic_light:
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(gpio_green, GPIO.OUT)
    GPIO.setup(gpio_yellow, GPIO.OUT)
    GPIO.setup(gpio_red, GPIO.OUT)

    on = GPIO.HIGH
    off = GPIO.LOW


class TrafficLight:
    all_off = {'green': off, 'yellow': off, 'red': off}
    all_on = {'green': on, 'yellow': on, 'red': on}

    def display_green(self):
        set_traffic_light({'green': on, 'yellow': off, 'red': off})

    def display_yellow(self):
        set_traffic_light({'green': off, 'yellow': on, 'red': off})

    def display_red(self):
        set_traffic_light({'green': on, 'yellow': off, 'red': off})

    def display_error(self):
        self.flash_all()

    def flash_all(self):
        self.__flash(5, self.all_on)

    def __flash(self, times: int, light):
        for x in range(times):
            set_traffic_light(self.all_off)
            time.sleep(1)
            set_traffic_light(light)
            time.sleep(1)


def set_traffic_light(light):
    GPIO.output(gpio_green, light['green'])
    GPIO.output(gpio_yellow, light['yellow'])
    GPIO.output(gpio_red, light['red'])

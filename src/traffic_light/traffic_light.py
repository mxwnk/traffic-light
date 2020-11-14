from config import gpio_green, gpio_yellow, gpio_red, use_fake_traffic_light

if not use_fake_traffic_light:
    import RPi.GPIO as GPIO


class TrafficLight:
    green = gpio_green
    yellow = gpio_yellow
    red = gpio_red

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_green, GPIO.OUT)
        GPIO.setup(gpio_yellow, GPIO.OUT)
        GPIO.setup(gpio_red, GPIO.OUT)

    def display_green(self):
        GPIO.output(gpio_green, GPIO.HIGH)
        GPIO.output(gpio_yellow, GPIO.LOW)
        GPIO.output(gpio_red, GPIO.LOW)

    def display_yellow(self):
        GPIO.output(gpio_yellow, GPIO.HIGH)
        GPIO.output(gpio_green, GPIO.LOW)
        GPIO.output(gpio_red, GPIO.LOW)

    def display_red(self):
        GPIO.output(gpio_red, GPIO.HIGH)
        GPIO.output(gpio_yellow, GPIO.LOW)
        GPIO.output(gpio_green, GPIO.LOW)

    def display_error(self, error):
        print(error)
        GPIO.output(gpio_red, GPIO.HIGH)
        GPIO.output(gpio_yellow, GPIO.HIGH)
        GPIO.output(gpio_green, GPIO.HIGH)

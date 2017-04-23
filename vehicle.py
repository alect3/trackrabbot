import time
import RPi.GPIO as GPIO

STEERING_PIN = 21
MOTOR_PIN = 2

class Vehicle:
    def __init__(self):
        self.start_time = time.clock()
        last_distance = 0.0
        last_time = 0.0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(STEERING_PIN, GPIO.OUT)
        GPIO.setup(MOTOR_PIN, GPIO.OUT)

        self.steer_gpio = GPIO.PWM(STEERING_PIN, 100)
        self.motor_gpio = GPIO.PWM(MOTOR_PIN, 100)

        self.steer_gpio.start(50)
        self.motor_gpio.start(50)

    def __del__(self):
        self.halt()

    def halt(self):
        self.steer_gpio.stop()
        self.motor_gpio.stop()
        GPIO.cleanup()
        

    def get_time(self):
        return self.clock() - self.start_time

    # TODO: Plug in interface to speed sensor
    def get_distance(self):
        return 2.0 * self.get_time() 

    # TODO: Plug in interface to speed sensor
    def get_velocity(self):
        delta_distance = self.get_distance() - self.last_distance
        delta_time = self.get_time() - self.last_time
        return delta_distance/delta_time

    # TODO: GPIO interface
    def set_motor(self, pwm):
        self.motor_gpio.ChangeDutyCycle(pwm)

    # TODO: GPIO interface
    def set_steering(self, pwm):
        self.steer_gpio.ChangeDutyCycle(pwm)

import time

class Vehicle:
    def __init__(start_time):
        self.start_time = start_time

    # vehicle moves at 2ms
    # TODO: Plug in interface to speed sensor
    def get_distance(self):
        return 2.0 * (self.clock() - self.start_time)

    # TODO: Plug in interface to speed sensor
    def get_velocity(self):
        return 2.0

    # TODO: GPIO interface
    def set_motor(self, pwm):
        pass

    # TODO: GPIO interface
    def set_steering(self, pwm):
        pass

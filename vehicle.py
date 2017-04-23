import time

class Vehicle:
    def __init__(start_time):
        self.start_time = time.clock()
        last_distance = 0.0
        last_time = 0.0

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
        pass

    # TODO: GPIO interface
    def set_steering(self, pwm):
        pass

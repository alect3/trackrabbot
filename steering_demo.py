from vehicle import Vehicle
from race import Race
from line_tracker import LineTracker, LineTrackerException 
from velocity_pid import VelocityPID
from steering_pid import SteeringPID
from utils import calc_required_velocity

import sys

def main_loop(race):
    current_distance = 0

    vehicle = Vehicle()
    line_tracker = LineTracker()
    velocity_pid = VelocityPID()
    steering_pid = SteeringPID()

    while True:
        # get real world position relative to line
        try:
            offset = line_tracker.get_position()
        except LineTrackerException, e:
            print e.message()
            vehicle.halt()
            return
       
        # pass angle and offset to steering pid
        steering_pid.update_current_position(offset)

        # request new pwm from steering PID
        steering_pwm = steering_pid.get_required_pwm() 

vehicle.halt()

if __name__ == "__main__":
    main_loop(race)

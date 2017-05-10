from vehicle import Vehicle
from line_tracker import LineTracker, LineTrackerException 
from velocity_pid import VelocityPID
from steering_pid import SteeringPID
from utils import calc_required_velocity

import sys
import time

def main_loop():
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
	    continue
	if offset == None:
	    continue
       
        # pass angle and offset to steering pid
        # steering_pid.update_position(offset)

        # request new pwm from steering PID
        steering_pwm = min(max(-offset + 200, 0),400)/4
        print "steering pwm".format(steering_pwm)

	vehicle.set_steering(steering_pwm)

if __name__ == "__main__":
    main_loop()

from vehicle import Vehicle
from race import Race
from line_tracker import LineTracker, LineTrackerException 
from velocity_pid import VelocityPID
from steering_pid import SteeringPID
from utils import calc_required_velocity

import sys
import json

def main_loop(race):
    current_distance = 0

    vehicle = Vehicle()
    line_tracker = LineTracker()
    velocity_pid = VelocityPID()
    steering_pid = SteeringPID()

    next_checkpoint = race.get_next_checkpoint(current_distance)
    while next_checkpoint:
        while current_distance < next_checkpoint.distance:
            # get distance & time
            current_distance = vehicle.get_distance()

            # get velocity 
            vehicle.get_velocity()
         
            # get required velocity
            required_velocity = calc_required_velocity(next_checkpoint, time_passed, current_distance)

            # pass velocity and required velocity to velocity PID
            velocity_pid.update_velocity(current_velocity)
            velocity_pid.update_required_velocity(required_velocity)

            # get real world position relative to line
            try:
                offset = line_tracker.get_position()
            except LineTrackerException, e:
                print e.message()
                vehicle.halt()
                return
           
            # pass angle and offset to steering pid
            steering_pid.update_current_position(offset, angle)

            # request new pwm from velocity PID
            motor_pwm = velocity_pid.get_required_pwm()

            # request new pwm from steering PID
            steering_pwm = steering_pid.get_required_pwm() 

            # set steering pwm
            vehicle.set_motor(motor_pwm)

            # set motor pwm
            vehicle.set_steering(steering_pwm)

        # update checkpoint
        next_checkpoint = race.get_next_checkpoint(current_distance)
    vehicle.halt()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: {} <race_file.json>'.format(sys.argv[0])
    race_file = open(sys.argv[1])
    race = Race(**json.loads(race_file.read()))
    main_loop(race)

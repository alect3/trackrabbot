from vehicle import Vehicle
from line_tracker import LineTracker
from velocity_pid import VelocityPID
from steering_pid import SteeringPID

import time

def setup():
    # load race profile
    # process race profile
    # load steering pwm calibrations
    # load velocity pwm calibrations
    # load velocity sensor calibrations

def main_loop(race_distance):
    current_distance = 0
    start_time = time.clock()

    vehicle = Vehicle(start_time)
    line_tracker = LineTracker()
    velocity_pid = VelocityPID()
    steering_pid = SteeringPID()

    while current_distance < race_distance:
        # get distance & time
        current_distance = vehicle.get_distance()
        current_time = time.clock()

        # get velocity 
        vehicle.get_velocity(current_time)
     
        # get desired velocity
        desired_velocity = get_desired_velocity(current_time)

        # pass velocity and desired velocity to velocity PID
        velocity_pid.update_velocity(current_velocity)
        velocity_pid.update_desired_velocity(desired_velocity)

        # get real world position relative to line
        offset, angle = line_tracker.get_position()
       
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

if __name__ == "__main__":
    main_loop()

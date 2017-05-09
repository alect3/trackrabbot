from vehicle import Vehicle
import time

vehicle = Vehicle()
for i in xrange(600,1000,1):
    pwm = i/100.0
    print '{}'.format(pwm)
    vehicle.set_steering(pwm)
    time.sleep(0.01)

for i in xrange(1000,600,-1):
    pwm = i/100.0
    print '{}'.format(pwm)
    vehicle.set_steering(pwm)
    time.sleep(0.01)

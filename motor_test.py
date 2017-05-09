from vehicle import Vehicle
import time

vehicle = Vehicle()
#vehicle.set_motor(7.3)
time.sleep(3)
for i in xrange(730,800,1):
    pwm = i/100.0
    print '{}'.format(pwm)
    vehicle.set_motor(pwm)
    time.sleep(0.1)

from vehicle import Vehicle
import time

vehicle = Vehicle()
for i in xrange(100,101,10):
    print '{}'.format(i)
    vehicle.set_motor(i)
    time.sleep(5)

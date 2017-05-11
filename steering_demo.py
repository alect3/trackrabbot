from vehicle import Vehicle
from line_tracker import LineTracker, LineTrackerException 
from velocity_pid import VelocityPID
from steering_pid import SteeringPID
from utils import calc_required_velocity

import cv2
import sys
import time
from flask import Flask, render_template, Response
from threading import Thread

app = Flask(__name__)

vehicle = Vehicle()
if len(sys.argv) > 1:
    line_tracker = LineTracker(sys.argv[1])
else:
    line_tracker = LineTracker()
velocity_pid = VelocityPID()
steering_pid = SteeringPID()
steering_pid.set_PID(10,4.4,100)

def video_feed():
    while True:
        with line_tracker.img_mutex: 
            if line_tracker.img != None:
                ret, jpeg = cv2.imencode('.jpg',line_tracker.img)
                yield(b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + jpeg.tostring() + b'\r\n\r\n')

@app.route('/')
def index():
    return Response(video_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

def main_loop():
    current_distance = 0

    while True:
        # get real world position relative to line
        try:
            offset = line_tracker.get_position()
        except LineTrackerException, e:
	    continue
	if offset == None:
	    continue
       
        # pass angle and offset to steering pid
        steering_pid.update_position(offset)

        # request new pwm from steering PID
        # steering_pwm = min(max(-offset + 200, 0),400)/4
	steering_pwm = steering_pid.get_required_pwm()
        print "steering pwm {}".format(steering_pwm)

	vehicle.set_steering(steering_pwm)

if __name__ == "__main__":
    video = False
    if video:
        t = Thread(target = main_loop)
	t.daemon = True
	t.start()
	app.run(host='0.0.0.0',debug=False)
    else:
        main_loop()   

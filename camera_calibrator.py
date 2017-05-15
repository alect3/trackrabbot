import cv2
from flask import Flask, render_template, Response
from threading import Thread, Lock

app = Flask(__name__)

cap = cv2.VideoCapture(0)
thresh = 0.5
thresh_mutex = Lock()

def video_feed():
    while True:
        _, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        with thresh_mutex:
            ret, img = cv2.threshold(img,thresh*255,255,cv2.THRESH_BINARY)
        ret, jpeg = cv2.imencode('.jpg',)
        yield(b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + jpeg.tostring() + b'\r\n\r\n')

@app.route('/')
def index():
    return Response(video_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

def change_thresh():
    while True:
        t = float(raw_input())
        if not (t > 0 and t < 1.0):
            print "invalid input"
            continue
        with thresh_mutex:
            thresh = t 

if __name__ == "__main__":
    t = Thread(target = main_loop)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0',debug=False)

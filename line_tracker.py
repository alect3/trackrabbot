import cv2
from multiprocessing import Lock
from threading import Thread
import copy
import time


center = [240, 240, 240]

class LineTrackerException(Exception):
    pass

class ImageReadException(LineTrackerException):
    pass

class NoLineFoundException(LineTrackerException):
    pass

def line_points(gray,center,line):
    width = gray[1].__len__()
    
    pos_x1 = 0
    pos_x2 = 0
    thresh = 180
    thresh,temp= cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#auto thresholding
	
	#find right side of line
    while((gray[line][(center)+pos_x1]>thresh)&(pos_x1<300)&((center+pos_x1)<(width-1))): 
        pos_x1 = pos_x1+1
	#find left side of line
    while((gray[line][(center)-pos_x2]>thresh)&(pos_x2<300)&((center-pos_x2)>0)):
        pos_x2 = pos_x2+1 
    
    
    pos_x2 = center -pos_x2    
    pos_x1 = center +pos_x1
    if pos_x1 >=width: #make sure its with in the screen size
        pos_x1 = width-1
    center = ((pos_x1)+(pos_x2))/2 #update center
    
    return pos_x1,pos_x2,center



def find_line_offset(img):
	#initalizing
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grayscale 
    #image width and height
	width = img[1].__len__()
    height = img.__len__()
    # center = [width/2,width/2,width/2] #initial center points is set to center of image
    line = [height/4,height/2,3*height/4] #line heights
    left = [0,0,0]
    right = [0,0,0]
    
    NOL = 3 #number of lines
    line_width = [0,0,0]
    
	###calculate###
    for i in range(0,NOL):
        #(left,right,line) calculate left,right and center points of line at line number
        right[i],left[i],center[i]=line_points(img,center[i],line[i])
	line_width[i] = right[i] - left[i]
    
	
	###logic###
    found_l = line_width[0]<line_width[1] and line_width[1]<line_width[2] # and (center[0]<center[1] and center[1]<center[2] or center[2]<center[1] and center[1]<center[0])
    
    gradient_x = center[0]-center[NOL-1]
    gradient_y = line[NOL-1] - line[0]
    gradient = gradient_y/gradient_x if gradient_x else 0
    if not found_l:
    	return None
    return center[NOL-1] - 0.5 * width
	

class LineTracker():
    def __init__(self, video_file=''): 
        self.cap = cv2.VideoCapture(video_file if video_file else 0)
        self.img_mutex = Lock()
	self.img = []
	self.img_read_success = False
	self.grab_img_thread_terminate = False
	self.grab_img_thread = Thread(target = self.grab_img)
	self.grab_img_thread.daemon = True
	self.grab_img_thread.start()

    def __del__(self):
	self.cap.release()
	with self.img_mutex:
	    self.grab_img_thread_terminate = True
	self.grab_img_thread.join()
	print "grab image thread terminated"

    def grab_img(self):
	terminate = False
        while not terminate:
            with self.img_mutex:
                self.img_read_success, self.img = self.cap.read()
	        terminate = self.grab_img_thread_terminate
	        time.sleep(0.01)

    def get_position(self):
	with self.img_mutex:
            if not self.img_read_success:
                raise ImageReadException("Image from camera could not be read")
            img = copy.deepcopy(self.img)
        offset = find_line_offset(img)
        if offset == None:
            raise NoLineFoundException("Line could not be located in image")
            for i in xrange(3):
	        center[i] = (centre[i] + 10) % 480
	return offset

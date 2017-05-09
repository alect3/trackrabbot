import cv2

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

    while((gray[line][(center)+pos_x1]>thresh)&(pos_x1<300)&((center+pos_x1)<(width-1))):
        pos_x1 = pos_x1+1
    while((gray[line][(center)-pos_x2]>thresh)&(pos_x2<300)&((center-pos_x2)>0)):
        pos_x2 = pos_x2+1 
    
    
    pos_x2 = center -pos_x2    
    pos_x1 = center +pos_x1
    if pos_x1 >=width:
        pos_x1 = width-1
    center = ((pos_x1)+(pos_x2))/2 #update center
    
    return pos_x1,pos_x2,center

def find_line_offset(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #errors here #convert to grayscale 
    width = img[1].__len__()
    height = img.__len__()#image height
    # center = [width/2,width/2,width/2] #initial center points is set to center of image
    line = [height/4,height/2,3*height/4] #line heights
    left = [0,0,0]
    right = [0,0,0]
    
    NOL = 3 #number of lines
    width = [0,0,0]
    
    for i in range(0,NOL):
        #(left,right,line) calculate left,right and center points of line at line number
        right[i],left[i],center[i]=line_points(img,center[i],line[i])
    
        #draw
        start = line[i]-100
        end = line[i]+100
        img = camera_draw(img,left[i],right[i],center[i],start,end)
        width[i] = right[i]-left[i]
        
    found_l = False
    
    if width[0]<width[1]<width[2]:
        if center[0]<center[1]<center[2]:
            found_l = True
        elif center[2]<center[1]<center[0]:
            found_l = True
    gradient_x = center[0]-center[NOL-1]
    gradient_y = line[NOL-1] - line[0]
    gradient = gradient_y/gradient_x if gradient_x else 0
    if not found_l:
    	return None
    return center[NOL/2] - 0.5 * width

class LineTracker() 
    def __init__(self): 
	self.cap = cv2.VideoCapture(0)

    def __del__(self):
	self.cap.release()

    def get_position():
	success, image = self.cap.read()
        if not success:
            raise ImageReadException("Image from camera could not be read")
        offset = find_line_offset(img)
        if offset == None:
            raise NoLineFoundException("Line could not be located in image")

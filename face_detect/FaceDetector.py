#refer to
#http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection
#2016-4-26
import numpy as np
import cv2

class FaceDetector:
    def __init__(self):
        #init the classifier class with the trained data
        self.face_cascade= cv2.CascadeClassifier("/home/rmqlife/opencv/data/haarcascades/haarcascade_frontalface_default.xml")

    def detectAndDraw(self,img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray=cv2.equalizeHist(gray)
        #get faces
        faces=self.face_cascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
        #draw rects
        for (x,y,w,h) in faces:
	        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	     
if __name__=='__main__':
    #image init
    img=cv2.imread('/home/rmqlife/Pictures/Webcam/2016-04-26-115422.jpg')
    fd=FaceDetector()
    fd.detectAndDraw(img)
    #show
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

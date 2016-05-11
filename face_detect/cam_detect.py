#refer to
#http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
#http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection
#2016-4-26
import numpy as np
import cv2
import FaceDetector

try:
    cap = cv2.VideoCapture(1)
except:
    cap = cv2.VideoCapture(0)

fd=FaceDetector.FaceDetector()

while (True):
    ret, img = cap.read()
    fd.detectAndDraw(img)
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()

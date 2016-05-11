# reference:
# http://www.learnopencv.com/seamless-cloning-using-opencv-python-cpp/
# http://www.irisa.fr/vista/Papers/2003_siggraph_perez.pdf
# 2016-4-28

import cv2
import numpy as np

imgA = cv2.imread("wood-texture.jpg")
imgB = cv2.imread("iloveyouticket.jpg")

# create an all white mask
mask = 255 * np.ones(imgB.shape, imgB.dtype)

(hA, wA)= imgA.shape[:2]
center = (wA/2, hA/2)

c1 = cv2.seamlessClone(imgB, imgA, mask, center, cv2.NORMAL_CLONE)
c2 = cv2.seamlessClone(imgB, imgA, mask, center, cv2.MIXED_CLONE)
cv2.imshow("normal clone",c1)
cv2.imshow("mixed clone",c2)
cv2.waitKey(0)

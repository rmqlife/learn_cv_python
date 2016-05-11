# reference
# http://docs.opencv.org/3.1.0/d7/d4d/tutorial_py_thresholding.html#gsc.tab=0
# http://www.pyimagesearch.com/2015/08/24/resolved-matplotlib-figures-not-showing-up-or-displaying/
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./test.jpg',0)
img = cv2.medianBlur(img, 5)

# global thresholding
ret1, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2, th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian Filtering
blur = cv2.GaussianBlur(img, (5,5), 0)
ret3, th3 = cv2.threshold(blur,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images = [img, 0,  th1,
          img, 0,  th2,
          blur,0,  th3] 

titles = ['Original', 'Histogram', "Global",
           'Original', 'Histogram', "Ostu",
           'Gaussian filtered', 'Histogram', 'Ostu']

for i in xrange(3):
    plt.subplot(3,3,i*3+1), plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    
    plt.subplot(3,3,i*3+2), plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    
    plt.subplot(3,3,i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    
plt.show()

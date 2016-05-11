# reference: http://docs.opencv.org/3.1.0/dc/dff/tutorial_py_pyramids.html
# 2016-4-28

import cv2
import numpy as np

class PyramidBlend:
    # left image, right image, amount of layers
    # for horizontal blend, assert imgA.shape same with imgB.shape
    def blend(self,imgA,imgB,layer_amount=6,width_percent=0.5):
        lpA = self.laplacianPyramid(imgA,layer_amount)
        lpB = self.laplacianPyramid(imgB,layer_amount)
        # layers
        ls = []
        for lA,lB in zip(lpA,lpB):
            #ASSERT lA and lB is in the same size
            h,w,d = lA.shape # height, width, depth
            #ALERT 0:w/2 w/2: is different, using different half of each image
            l = np.hstack((lA[:,0: int(w * width_percent)], lB[:,int(w * width_percent):])) 
            ls.append(l)
        
        # showPyramid(ls)
        # reconstruct
        b = ls[0]
        for i in xrange(1,len(lpA)):
            b = cv2.pyrUp(b)
            b = cv2.add(b, ls[i])
        return b 
        
    def simpleBlend(self,imgA,imgB,width_percent=0.5):
        w =  imgA.shape[1]
        return np.hstack((imgA[:,0: int(w * width_percent)], imgB[:,int(w * width_percent):]))  
         
    def gaussianPyramid(self, img, amount):
        # generate Gaussian pyramid for image
        G =  img.copy()
        gp = [G] # gaussian pyramid
        for i in xrange(amount):
            G = cv2.pyrDown(G)
            gp.append(G)
        return gp    
        
    def laplacianPyramid(self, img, amount):
        # generate Laplacian Pyramid for image
        gp = self.gaussianPyramid(img,amount)
        lp = [gp[amount-1]]
        for i in xrange(amount-1,0,-1): #amount-1...,2,1
            ge = cv2.pyrUp(gp[i])
            l = cv2.subtract(gp[i-1],ge)
            lp.append(l)
        return lp
        
    def showPyramid(self, p):
        for i in p:
            cv2.imshow("img", i)
            cv2.waitKey(0)
        pass
        
if __name__=="__main__":
    imgA =  cv2.imread('apple.jpg')
    imgB =  cv2.imread('orange.jpg') 
    
    b = PyramidBlend().blend(imgA,imgB,layer_amount=7,width_percent=0.2)
    cv2.imshow('result',b)
    sb = PyramidBlend().simpleBlend(imgA,imgB,width_percent=0.2)
    cv2.imshow('simple',sb)
    
    cv2.waitKey(0)
    

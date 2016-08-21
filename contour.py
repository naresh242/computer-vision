'''
Created on Aug 21, 2016

@author: hp-pc
'''
from numpy import dtype
import argparse
import cv2
import numpy as np
import mahotas
#from histequalization import draw_hist
from matplotlib import pyplot as plt

def cannyedge(image):
    
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blured=cv2.GaussianBlur(image,(5,5),0)
    thresh=cv2.Canny(blured,30,150)
   
   
    return thresh
image = cv2.imread("E:/naresh/learning/books/pyimage/Books/ppocv/code/images/coins.png")
thresh=cannyedge(image)

cnts,_=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
coins=image.copy()   
cv2.drawContours(coins,cnts,-1,(0,0,255),2)
cv2.imshow("contours",np.hstack((image,coins)))
for i,c in enumerate(cnts):
    (x,y,h,w)=cv2.boundingRect(c)
    coin=image[y:y+h,x:x+w]
    mask=np.zeros(image.shape[:2],dtype="uint8")
    
    ((cx,cy),r)=cv2.minEnclosingCircle(c)
    
    cv2.circle(mask,(int(cx),int(cy)),int(r),255,-1)
    mask=mask[y:y+h,x:x+w]
    masked=cv2.bitwise_and(coin,coin,mask=mask)
    cv2.imshow("coin",np.hstack((coin,masked)))
    cv2.waitKey(0)
    
cv2.waitKey(0)
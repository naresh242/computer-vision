
from numpy import dtype
import argparse
import cv2
import numpy as np
import mahotas
from histequalization import draw_hist
from matplotlib import pyplot as plt

def tresholding():
    image = cv2.imread("E:/naresh/learning/books/pyimage/Books/ppocv/code/images/coins.png")
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blured=cv2.GaussianBlur(image,(3,3),0)
    cv2.imshow("blured",np.hstack((image,blured)))
    T,treshed=cv2.threshold(blured,155,255,cv2.THRESH_BINARY)
    T,invtreshed=cv2.threshold(blured,155,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("treshed",np.hstack((treshed,invtreshed)))
    coins=cv2.bitwise_and(image,image,mask=invtreshed)
    cv2.imshow("coins",coins)    
    cv2.waitKey(0)
    
    
'''
adaptive thresholding
'''
def adaptivethresholding():        
    image = cv2.imread("E:/naresh/learning/books/pyimage/Books/ppocv/code/images/coins.png")
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blured=cv2.GaussianBlur(image,(5,5),0)
    
    admeantreshed=cv2.adaptiveThreshold(blured,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,4)
    adguasstreshed=cv2.adaptiveThreshold(blured,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,3)
    cv2.imshow("treshed",np.hstack((image,admeantreshed,adguasstreshed)))
    # coins=cv2.bitwise_and(image,image,mask=invtreshed)
    #cv2.imshow("coins",coins)    
    cv2.waitKey(0)   
    
'''    
otsu thresholding
'''
def thresholding_otsu():    
    image = cv2.imread("E:/naresh/learning/books/pyimage/Books/ppocv/code/images/coins.png")
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blured=cv2.GaussianBlur(image,(5,5),0)
    draw_hist(fimage=blured,ftitle="blured",fmask=None)
    plt.show()
    T=mahotas.thresholding.otsu(blured)
    print(T)
    blured[blured>T]=255
    blured[blured<=T]=0
    
    cv2.imshow("treshed",np.hstack((image,blured)))
    # coins=cv2.bitwise_and(image,image,mask=invtreshed)
    #cv2.imshow("coins",coins)    
    cv2.waitKey(0)                
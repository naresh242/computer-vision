'''
Created on Aug 21, 2016

@author: hp-pc
'''
from numpy import dtype
import argparse
import cv2
import numpy as np
import mahotas
from histequalization import draw_hist
from matplotlib import pyplot as plt

def cannyedge():
    image = cv2.imread("E:/naresh/learning/books/pyimage/Books/ppocv/code/images/coins.png")
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blured=cv2.GaussianBlur(image,(5,5),0)
    thresh=cv2.Canny(blured,30,150)
    cv2.imshow("edge",np.hstack((image,blured,thresh)))
    cv2.waitKey(0)
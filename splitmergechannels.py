'''
Created on Aug 20, 2016

@author: hp-pc
'''
from __future__ import print_function
import argparse
import cv2
import numpy as np

#E:/naresh/learning/books/pyimage/Books/ppocv/code/images/trex.png
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "help")
#args = vars(ap.parse_args())
    
image = cv2.imread("E:/naresh/learning/books/pyimage/Books/ppocv/code/images/trex.png")

b,g,r=cv2.split(image)
cv2.imshow("blue",b)
orimage=cv2.merge([b,g,r])
cv2.imshow("ori",orimage)
cv2.waitKey(0)
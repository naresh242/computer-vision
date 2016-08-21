'''
@author: hp-pc
'''
from __future__ import print_function
from matplotlib import pyplot as plt

from numpy import dtype
import argparse
import cv2
import numpy as np


def draw_hist(image,title,mask=None):
    chans=cv2.split(image)
    colors=("b","g","r")
    plt.Figure()
    plt.title(title)
    plt.xlabel("pixel")
    plt.ylabel("pixel den")
    for col,chan in zip(colors,chans):
        hist=cv2.calcHist([chan],[0],mask,[256],[0,256])
        plt.plot(hist,color=col)
    plt.xlim([0,256])
    
        
image = cv2.imread("E:/naresh/learning/books/pyimage/Books/ppocv/code/images/beach.png")

zeros=np.zeros(image.shape[:2],dtype = "uint8")
centre=(zeros.shape[0]//2,zeros.shape[1]//2)
print(centre)
print(zeros.shape)
print(image.shape)

cv2.rectangle(zeros,(centre[1]-30,centre[0]-30),(centre[1]+30,centre[0]+30),255,-1)
masked=cv2.bitwise_and(image,image,mask=zeros)
cv2.imshow("masked",masked)
draw_hist(image,"scene",mask=zeros)
plt.show()


#cv2.waitKey(0)
        
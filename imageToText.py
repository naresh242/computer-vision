'''
Created on Oct 18, 2016

@author: NA347632
'''
import sys
import requests
import pytesseract
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO
import cv2

def process_image(url):
    
    image = _get_image(url)
    
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("gray",image)
    cv2.waitKey(0)
    bw=cv2.adaptiveThreshold(image, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, -2)
    hor=bw.copy()
    ver=bw.copy()
    
    #image.filter(ImageFilter.SHARPEN)
    image =Image.fromarray(image)
    print type(image)
    
    return pytesseract.image_to_string(image)

def _get_image(url):
    return cv2.imread(url)

    #return Image.open(url)


imgurl="C:/Users/na347632/Desktop/OCR/sample1.jpg"
umurl="https://realpython.com/images/blog_images/ocr/sample1.jpg"
text=process_image(imgurl)
print(text)

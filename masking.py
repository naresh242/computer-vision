from __future__ import print_function
import argparse
import cv2
import numpy as np

#E:/naresh/learning/books/pyimage/Books/ppocv/code/images/trex.png
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "help")
#args = vars(ap.parse_args())

image = cv2.imread("E:/naresh/learning/books/pyimage/Books/ppocv/code/images/trex.png")
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)

cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75),255, -1)
masked = cv2.bitwise_and(image,image,mask=mask)

cv2.imshow("Mask", masked)
cv2.imshow("original", image)

cv2.waitKey(0)
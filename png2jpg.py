from __future__ import print_function
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "help")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("trex.jpg",image)
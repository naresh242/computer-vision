# of kernels sizes that will be applied to the image
# load the image and convert it to grayscale
image = cv2.imread("local/image.jpg"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]
 
# loop over the kernels and apply an "opening" operation to the image
for kernelSize in kernelSizes:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
	cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
	cv2.waitKey(0)

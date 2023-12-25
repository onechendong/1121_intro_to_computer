import cv2
import numpy as np

## show original pic
image = cv2.imread("TW.jpg")
cv2.imshow("Original", image) # show original pic
cv2.waitKey(0) # press Enter
 
## use numpy to convert pic to grayscale
img_array = np.array(image)
grayscale_array = np.mean(img_array, axis=-1, dtype=np.uint8) # convert pic by use "gray = (r + g + b) / 3"
cv2.imshow("Grayscale(numpy)", grayscale_array) # show grayscale pic
cv2.waitKey(0) # press Enter

## use cv2 to convert pic to grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert pic to grayscale and put it into "grayscale"
cv2.imshow("Grayscale(cv2)", grayscale) # show grayscale pic
cv2.waitKey(0) # press Enter

## binarization
_, binary_image = cv2.threshold(grayscale, 244, 255, cv2.THRESH_BINARY) # we dont need retval; we just need image (pixel intensity value <244: 0（black), >= 244: 255（white))
cv2.imshow("Binarization", binary_image) # show binary pic
cv2.waitKey(0) # press Enter
cv2.destroyAllWindows() # exit
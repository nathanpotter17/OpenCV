import numpy as numpy
import cv2

img = cv2.imread('g3.png', 1)

img = cv2.line(img, (0,0), (255,255), (0,0,255), 3) #BGR color space (img, coord1, coord2, color, thickness)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
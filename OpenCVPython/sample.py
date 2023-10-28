import cv2

print(cv2.__version__)


# img mode 1 with color 0 as grayscale -1 as is alpha

# write new files
# cv2.imwrite('copyimage', img)


img = cv2.imread('./g3.png', -1) 

print(img)

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
  cv2.destroyAllWindows()
elif k == ord('s'):
  cv2.imwrite('copyimage', img)
  cv2.destroyAllWindows()
# Note:
# -1, v2.IMREAD_COLOR :loads a color image. Any transparency of image will be neglected. it's the default flag.
# 0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
import cv2

img = cv2.imread('assets/test.png', 1) #display the image

# img = cv2.resize(img, (400, 400)) #resize image by pixels
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) #resize image by scaling
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) #rotate the image 

cv2.imwrite('test_rotate.png', img)


cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
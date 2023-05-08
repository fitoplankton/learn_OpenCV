# note :
# OpenCV used Blue Green Red (BRG)
import cv2
import random

img = cv2.imread('assets/test.png', -1)

# print(img[135][50:500]) #accessing pixel value
# # print(img)
# # print(type(img))
print(img.shape)

#Changing Pixel Color (shape (3,))
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#Copying and Pasting Parts of Image
tag = img[50:100, 100:300]
img[5:55, 150:350] = tag

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
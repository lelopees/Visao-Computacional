import cv2
import numpy as np

img_lg = cv2.imread('IN1LG.jpg')
img_poco = cv2.imread('IN1POCO.jpg')

print('LG = ',img_lg.shape)
print('POCO = ', img_poco.shape)

#cv2.imshow('img_lg', img_lg)
#cv2.imshow('img_poco', img_poco)

cv2.waitKey(0)
import cv2 
import numpy as np

mask_ref = cv2.imread('mask_ref.png')

mask_ref = cv2.resize(mask_ref, (0,0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(mask_ref, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(mask_ref, cv2.COLOR_BGR2GRAY)

print(gray.shape)

contours = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
print(contours[1])

print('NONE')

"""
for c in enumerate(contours):
    print(c)

    area = cv2.contourArea(c)
    print(area)
    #if area > 1000:
     #   cv2.drawContours(gray2, contours, i, (255, 0, 0), 3)
#cv2.imwrite('output3.jpg', gray2)
"""

contours = contours[0] if len(contours) == 2 else contours[1]
big_contour = max(contours, key=cv2.contourArea)

rotrect = cv2.minAreaRect(big_contour)
(center), (width,height), angle = rotrect
print(center)
print(width)
print(height)

box = cv2.boxPoints(rotrect)
boxpts = np.intp(box)
print(boxpts)
rotrect_img = mask_ref.copy()
imgLa = cv2.drawContours(rotrect_img,[boxpts],0,(0,0,255),1)


########
contours = cv2.findContours(gray2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contours))
print(contours[1])
contours = contours[0] if len(contours) == 2 else contours[1]
big_contour = max(contours, key=cv2.contourArea)

rotrect = cv2.minAreaRect(big_contour)
(center), (width,height), angle = rotrect
print(center)
print(width)
print(height)

box = cv2.boxPoints(rotrect)
boxpts = np.intp(box)
print(boxpts)
rotrect_img = mask_ref.copy()
imgLa2 = cv2.drawContours(rotrect_img,[boxpts],0,(0,0,255),1)

img2 = cv2.drawContours(gray, contours, -1, (0,255,75), 2) 
img2 = cv2.drawContours(gray, contours, 3, (0,255,75), 2) 

cv2.imshow('original', mask_ref)
cv2.imshow('imgLa', imgLa)
cv2.imshow('imgLa2', imgLa2)
cv2.imshow('img2', img2)

cv2.waitKey(0)
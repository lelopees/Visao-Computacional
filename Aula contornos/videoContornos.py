import cv2
import numpy as np
#capture.release()
cv2.destroyAllWindows()
capture = cv2.VideoCapture(0)
panel = np.zeros([100, 700], np.uint8)
cv2.namedWindow('panel')
def nothing(x):
    pass

cv2.createTrackbar('L - h', 'panel', 0, 179, nothing) #
cv2.createTrackbar('U - h', 'panel', 179, 179, nothing)

cv2.createTrackbar('L - s', 'panel', 0, 255, nothing)
cv2.createTrackbar('U - s', 'panel', 255, 255, nothing)

cv2.createTrackbar('L - v', 'panel', 0, 255, nothing)
cv2.createTrackbar('U - v', 'panel', 255, 255, nothing)

cv2.createTrackbar('S ROWS', 'panel', 0, 480, nothing) #start 
cv2.createTrackbar('E ROWS', 'panel', 480, 480, nothing) # end
cv2.createTrackbar('S COL', 'panel', 0, 640, nothing)
cv2.createTrackbar('E COL', 'panel', 640, 640, nothing)

while(True):

    ret, frame = capture.read()

    s_r = cv2.getTrackbarPos('S ROWS', 'panel')
    e_r = cv2.getTrackbarPos('E ROWS', 'panel')
    s_c = cv2.getTrackbarPos('S COL', 'panel')
    e_c = cv2.getTrackbarPos('E COL', 'panel')
    #print(frame.shape) = 480 , 640, 3 
    roi = frame[s_r: e_r, s_c: e_c]
    roi =  cv2.GaussianBlur(roi, (5, 5), 0) #sigma = 0
    hsv = cv2.cvtColor( roi, cv2.COLOR_RGB2HSV)    

    l_h = cv2.getTrackbarPos('L - h', 'panel')
    u_h = cv2.getTrackbarPos('U - h', 'panel')
    l_s = cv2.getTrackbarPos('L - s', 'panel')
    u_s = cv2.getTrackbarPos('U - s', 'panel')
    l_v = cv2.getTrackbarPos('L - v', 'panel')
    u_v = cv2.getTrackbarPos('U - v', 'panel')
    lower_green = np.array([l_h, l_s, l_v])
    upper_green = np.array([u_h, u_s, u_v])


    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)

    bg = cv2.bitwise_and( roi,  roi, mask=mask)
    fg = cv2.bitwise_and( roi,  roi, mask=mask_inv)
    gray = cv2.cvtColor(fg, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(gray,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)

        if area>20000:
            cv2.drawContours(fg, contours, -1, (0, 255, 0), 3)

        c = max(contours, key = cv2.contourArea)

        x,y,w,h = cv2.boundingRect(c)
        # draw the book contour (in green)
        cv2.rectangle(fg,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('bg', bg)
    cv2.imshow('fg', fg)
    cv2.imshow('panel', panel)

    if cv2.waitKey(30) == 27: #siradaki frame'e gecmeden once 30 ms bekle
        break

capture.release()
cv2.destroyAllWindows()

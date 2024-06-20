# IMPORTS
import cv2
import numpy as np

# READ VIDEO
cap = cv2.VideoCapture("video.mp4")

# GET FIRST FRAME
_, first_frame = cap.read()

# CONVERT FIRST FRAME TO GRAY
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

# BLUR GRAY FRAME
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

# LOOP
while True:

    # READ FRAME
    _, frame = cap.read()

    # CONVERT FRAME TO GRAY
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # BLUR  FRAME
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    
    # GET DIFFRERENCE BETWEEN FIRST FRAME AND ACTUAL
    difference = cv2.absdiff(first_gray, gray_frame)

    # THRESHOLD DIFFERENCE
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    
    # SHOW FIRST FRAME
    cv2.imshow("First frame", first_frame)

    # SHOW FRAME
    cv2.imshow("Frame", frame)

    # SHOW DIFFERENCE
    cv2.imshow("difference", difference)
    
    # WAITKEY
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


# RELEASE CAP
cap.release()

# DESTROY ALL WINDOWS
cv2.destroyAllWindows()
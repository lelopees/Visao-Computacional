# IMPORTS
import cv2
import numpy as np

# READ VIDEO
cap = cv2.VideoCapture("video.mp4")

# CREATE SUBTRACTOR
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

# LOOP
while True:
    
    # READ FRAME
    _, frame = cap.read()

    # CREATE MASK USING THE SUBTRACTOR AND ACTUAL FRAME
    mask = subtractor.apply(frame)

    # criar kernel
    kernel = np.ones((5,5), np.uint8)

     # opening
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=1)

    # dilatação 
    dilate = cv2.dilate(closing, kernel, iterations=1)

     # detectar contornos
    contours, h = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Desenhar contornos
    cv2.drawContours(frame, contours, -1, (255,0,0),3)

    # SHOW FRAME
    cv2.imshow("Frame", frame)
    # SHOW MASK
    cv2.imshow("dilate", dilate)

    # WAITKEY
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


# RELEASE CAP
cap.release()

# DESTROY ALL WINDOWS
cv2.destroyAllWindows()

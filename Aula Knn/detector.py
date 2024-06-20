# IMPORTS
import cv2
import numpy as np

# FUNCTIONS
def nothing(x):
    pass
# READ VIDEO
cap = cv2.VideoCapture(0)

digits = cv2.imread("digits.png", cv2.IMREAD_GRAYSCALE)
# CREATE WINDOW
cv2.namedWindow('trackbars')
cv2.createTrackbar("th", "trackbars", 127, 255, nothing)

rows = np.vsplit(digits, 50)
cells = []
for row in rows:
    row_cells = np.hsplit(row, 50)
    for cell in row_cells:
        cell = cell.flatten()
        cells.append(cell)

cells = np.array(cells, dtype=np.float32)

k = np.arange(10)
cells_labels = np.repeat(k, 250)

# KNN
knn = cv2.ml.KNearest_create()
knn.train(cells, cv2.ml.ROW_SAMPLE, cells_labels)

# LOOP
while(True):
    # READ FRAME
    _, frame = cap.read()
    th = cv2.getTrackbarPos("th", "trackbars")

    frame = frame[150:400, 100:400]

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    ret, thresh = cv2.threshold(gray,th,255,cv2.THRESH_BINARY_INV)

    kernel = np.ones((3,3),np.uint8)

    erosion = cv2.dilate(thresh,kernel,iterations = 1)

    cv2.imshow('erosion',erosion)
    

    contours, hierarchy = cv2.findContours(erosion,cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)

     # RUN ALL CONTOURS
    for i,cnt in enumerate(contours):

        test_cells = []
        # CONTOUR AREA
        area = cv2.contourArea(cnt)
        # CHECK IF AREA IS LARGE ENOUGH
        try:

            if area > 30 and area < 600:
                # BOUNDING RECT THE CONTOUR
                x,y,w,h = cv2.boundingRect(cnt)

                # DRAW RECT IN FRAME

                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                offs = 10
                crop = erosion[y-offs:y+h+offs, x-offs:x+w+offs]

                if crop.shape[0] > crop.shape[1]:
                    newW = (crop.shape[1]*20)/crop.shape[0]
                    crop = cv2.resize(crop, (int(newW), 20))

                else:
                    newW = (crop.shape[0]*20)/crop.shape[1]
                    crop = cv2.resize(crop, (20, int(newW)))



                #crop = cv2.add(img, crop)
                height, width = crop.shape
                
                x2 = height if height > width else width
                y2 = height if height > width else width

                square= np.zeros((x2,y2), np.uint8)

                square[int((y2-height)/2):int(y2-(y2-height)/2), int((x2-width)/2):int(x2-(x2-width)/2)] = crop

                #square = cv2.resize(square, (20, 20))

                test_cells.append(square.flatten())
                test_cells = np.array(test_cells, dtype=np.float32)

                #cv2.imshow('square',square)
                #cv2.imshow('crop',crop)
                ret, result, neighbours, dist = knn.findNearest(test_cells, k=1)
                cv2.putText(frame,str(int(result[0][0])),(x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA)

        except:
            pass




    cv2.imshow('thresh',thresh)


    # SHOW FRAME
    cv2.imshow('frame',frame)
    # WAITKEY
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

# RELEASE CAP
cap.release()

# DESTROY ALL WINDOWS
cv2.destroyAllWindows()
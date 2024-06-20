import cv2
import numpy as np

# funcoes
def nothing(x):
    pass

digits = cv2.imread('digits.png',0)

# dividindo em várias linhas
rows = np.vsplit(digits,50)
cells = []
for row in rows:
    # dividindo em várias colunas
    row_cell = np.hsplit(row, 50)
    # percorrendo cada imagem
    for cell in row_cell:
        #cv2.imshow('antes', cell)
        # transformando essa imagem em uma unica linha só
        cell = cell.flatten()
        #cv2.imshow('depois', cell)
        cells.append(cell)

cells = np.array(cells, dtype = np.float32)

k = np.arange(10)
cells_labels = np.repeat(k, 250)

knn = cv2.ml.KNearest_create()
knn.train(cells, cv2.ml.ROW_SAMPLE, cells_labels)


# criar de janeka de trackbars
cv2.namedWindow('trackbars')

# criar as trackbars

#trackbar_name: É o nome da trackbar.
#window_name: É o nome da janela onde a trackbar será exibida.
#start_value: É o valor inicial da trackbar.
#max_value: É o valor máximo que a trackbar pode atingir.
#callback: É uma função de retorno de chamada que será chamada sempre 
#que o valor da trackbar for alterado pelo usuário. Essa função é opcional.

cv2.createTrackbar('x', 'trackbars', 35, 800, nothing)
cv2.createTrackbar('y', 'trackbars', 90, 800, nothing)
cv2.createTrackbar('w', 'trackbars', 230, 800, nothing)
cv2.createTrackbar('h', 'trackbars', 290, 800, nothing)
cv2.createTrackbar('th', 'trackbars', 170, 255, nothing)

# capturar video
cap = cv2.VideoCapture(0)

while True:

    #recuperar trackbar
    x =cv2.getTrackbarPos('x', 'trackbars')
    y =cv2.getTrackbarPos('y', 'trackbars')
    w =cv2.getTrackbarPos('w', 'trackbars')
    h =cv2.getTrackbarPos('h', 'trackbars')
    th =cv2.getTrackbarPos('th', 'trackbars')

    #recuperar frame do video
    ret, frame = cap.read()

    roi = frame[y:h, x:w]

    # gray roi
    gray = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)

    # criar threhold
    ret, thresh = cv2.threshold(gray,th,255,cv2.THRESH_BINARY_INV)

     # criar kernel
    kernel = np.ones((5,5), np.uint8)

    # erosao
    erosion = cv2.dilate(thresh, kernel, iterations=1)

    erosion = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel, iterations=1)


    # detectar contornos
    contours, h = cv2.findContours(erosion,cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)
    
     # RUN ALL CONTOURS
    for i,cnt in enumerate(contours):

        test_cells = []
        # CONTOUR AREA
        area = cv2.contourArea(cnt)
        # CHECK IF AREA IS LARGE ENOUGH
        try:

            if area > 25:
                # BOUNDING RECT THE CONTOUR
                x,y,w,h = cv2.boundingRect(cnt)

                # DRAW RECT IN FRAME

                cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),2)
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
                cv2.putText(roi,str(int(result[0][0])),(x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA)

        except:
            pass

    cv2.imshow('thr', thresh) 

    # exibindo o frame
    cv2.imshow('roi', roi)

    if cv2.waitKey(1) == ord('q'):
        break

# libero o cap
cap.release()

# destruo todas as janelas
cv2.destroyAllWindows() 



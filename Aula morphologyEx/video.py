import cv2
import numpy as np

# funcoes
def nothing(x):
    pass

# criar de janeka de trackbars
cv2.namedWindow('trackbars')

# criar as trackbars

#trackbar_name: É o nome da trackbar.
#window_name: É o nome da janela onde a trackbar será exibida.
#start_value: É o valor inicial da trackbar.
#max_value: É o valor máximo que a trackbar pode atingir.
#callback: É uma função de retorno de chamada que será chamada sempre 
#que o valor da trackbar for alterado pelo usuário. Essa função é opcional.

cv2.createTrackbar('th', 'trackbars', 150, 255, nothing)
cv2.createTrackbar('ero', 'trackbars', 1, 10, nothing)
cv2.createTrackbar('dil', 'trackbars', 1, 10, nothing)
cv2.createTrackbar('open', 'trackbars', 1, 50, nothing)
cv2.createTrackbar('close', 'trackbars', 1, 50, nothing)

# capturar video
cap = cv2.VideoCapture(0)

while True:

    #recuperar trackbar
    th =cv2.getTrackbarPos('th', 'trackbars')
    ero =cv2.getTrackbarPos('ero', 'trackbars')
    dil =cv2.getTrackbarPos('dil', 'trackbars')
    open =cv2.getTrackbarPos('open', 'trackbars')
    close =  cv2.getTrackbarPos('close', 'trackbars')

    #recuperar frame do video
    ret, frame = cap.read()    

     # criar BLUR
    #blur = cv2.GaussianBlur(frame, (15,15), 0) 
    #cv2.imshow('blur', blur)

    # criar frame em preto e branco
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # EXIBIR GRAY
    #cv2.imshow('gray', gray)

    # criar threshold (100 = INTENSIDADE, 255 = LUZIMINDADE)
    ret, thres = cv2.threshold(gray, th, 255, cv2.THRESH_BINARY)

    # criar kernel
    kernel = np.ones((5,5), np.uint8)

    # erosao
    erosion = cv2.erode(thres, kernel, iterations=ero)

    # dilatação 
    dilate = cv2.dilate(thres, kernel, iterations=dil)

    # opening
    opening = cv2.morphologyEx(thres, cv2.MORPH_OPEN, kernel, iterations=open)

    closing = cv2.morphologyEx(thres, cv2.MORPH_CLOSE, kernel, iterations=close)
    
    # exibir erosao
    #cv2.imshow('erosion', erosion)

    #EXIBIR threshold
    cv2.imshow('thres', thres)

    # EXIBIR dilate
    #cv2.imshow('dilate', dilate)
    
    # EXIBIR opening
    cv2.imshow('opening', opening)

     # EXIBIR opening
    cv2.imshow('closing', closing)

    # exibindo o frame
    #cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# libero o cap
cap.release()

# destruo todas as janelas
cv2.destroyAllWindows() 



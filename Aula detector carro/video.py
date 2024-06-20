import cv2
import numpy as np

# capturar video
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('video.mp4')

subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

# criar loop infinito
while (True):
    # recuperar frame
    ret, frame = cap.read()

    mask = subtractor.apply(frame)
    
    # criar kernel
    kernel = np.ones((5,5), np.uint8)

     # opening
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    # TRANSFORMANDO os pontos cinzas em pontos brancos
    ret, mask = cv2.threshold(mask, 100,255, cv2.THRESH_BINARY)

    # dilatação (mais gordinho)
    mask = cv2.dilate(mask, kernel, iterations=1)
    
    # fechar os pontos que estão abertos
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    # detectar contornos da mask
    contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:        
        area = cv2.contourArea(cnt)
        if area > 1500:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255,0),2)

            # Desenhar contornos
            #cv2.drawContours(frame, cnt, -1, (255,0,0),3)
        print(area)   

    # mostrar frame    
    cv2.imshow('frame', frame)

    # mostrar mask    
    cv2.imshow('mask', mask)
    # recupera o botão apertado 
    key = cv2.waitKey(30)

    if key == ord('q'):
        break

# liberar o cache do cap
cap.release()

# destroi todas as janelas abertas
cv2.destroyAllWindows()
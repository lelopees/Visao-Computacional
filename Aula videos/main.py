import cv2

# capturar video
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('video_rua01.mp4')

# criar loop infinito
while (True):
    # recuperar frame
    ret, frame = cap.read()

    # se tem retorno
    if ret:
        # mostrar frame    
        cv2.imshow('frame', frame)

        roi = frame[400:550, 650:800]
        cv2.imshow('roi', roi) 

        img_resize = cv2.resize(frame, (600,600))
        cv2.imshow('resize', img_resize)

    # recupera o botão abertado 
    key = cv2.waitKey(30)

    if key == ord('q'):
        break

# liberar o cache do cap
cap.release()

# destroi todas as janelas abertas
cv2.destroyAllWindows()
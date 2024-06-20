import cv2

# capturar video
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)

# carregar o haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# criar loop infinito
while (True):
    # recuperar frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detectar faces na imagem

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        
        # roi da face (area de interesse)
        roi = frame[y:y+h,x:x+w]

        # para borrar: passando a imagem de um tamanho 5x5 
        # e depois para o tamnho original w,h

        roi = cv2.resize(roi, (5,5))

        roi = cv2.resize(roi, (w,h))
        # mostrar roi    
        cv2.imshow('roi', roi)

        frame[y:y+h, x:x+w] = roi
        # desenhar retangulo em volta da face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),3)

       
    # mostrar frame    
    #cv2.imshow('gray', gray)
    
    # mostrar frame    
    cv2.imshow('frame', frame) 

    # recupera o botão abertado 
    key = cv2.waitKey(30)

    if key == ord('q'):
        break

# liberar o cache do cap
cap.release()

# destroi todas as janelas abertas
cv2.destroyAllWindows()
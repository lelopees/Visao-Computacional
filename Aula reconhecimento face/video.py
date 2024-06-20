import cv2
import os
import numpy as np

def savePerson():
    global ultimoNome
    global boolsaveimg
    
    print('Qual o seu nome:')
    name = input()
    ultimoNome = name
    print(ultimoNome)
    boolsaveimg = True

def saveImg(img):
    if not os.path.exists('train'):
        os.makedirs('train')

    if not os.path.exists(f'train/{ultimoNome}'): 
        os.makedirs(f'train/{ultimoNome}')

    files = os.listdir(f'train/{ultimoNome}')
    cv2.imwrite(f'train/{ultimoNome}/{str(len(files))}.jpg', img)


def trainData():
    global recognizer
    global trained
    global persons

    trained = True
    persons = os.listdir('train')

    ids = []
    faces = []

    for i, p in enumerate(persons):
        for f in os.listdir(f'train/{p}'):
            img = cv2.imread(f'train/{p}/{f}', 0)
            faces.append(img)
            ids.append(i)

    recognizer.train(faces, np.array(ids))

ultimoNome = ''

boolsaveimg =False

trained = False

persons = []

saveCount = 0

# capturar video
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture()

ip = "https://192.168.200.105:8080/video"
cap.open(ip)

recognizer = cv2.face.LBPHFaceRecognizer_create()

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
        roi = gray[y:y+h,x:x+w] 
        roi = cv2.resize(roi,(50,50))          
        # desenhar retangulo em volta da face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0),2)

        if trained:
            idf, conf = recognizer.predict(roi)
            nameP = persons[idf]
            cv2.putText(frame, nameP, (x+23, y+23), 3,1, (255,255,255), 1 , cv2.LINE_AA)

        if boolsaveimg:
            saveImg(roi)
            saveCount += 1

        if saveCount > 50:
            boolsaveimg = False
            saveCount = 0

    # mostrar frame    
    #cv2.imshow('gray', gray)
    
    # mostrar frame    '
    cv2.imshow('frame', frame) 

    # recupera o botão abertado 
    key = cv2.waitKey(30)

    # salvar imagens
    if key == ord('s'):
        savePerson()

    if key == ord('t'):
        trainData()

    if key == ord('q'):
        break

# liberar o cache do cap
cap.release()

# destroi todas as janelas abertas
cv2.destroyAllWindows()
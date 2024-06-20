# IMPORTS
import numpy as np
import cv2
import os

# FUNCTIONS

def creatDir(name, path=''):
    # CHECK IF FOLDER EXISTS
    if not os.path.exists(f'{path}/{name}'):
        # IF NOT, CREATE
        os.makedirs(f'{path}/{name}')

def saveFace():
    # GET GLOBALS
    global saveface
    global lastName
    # SET SAVE FACE TRUE
    saveface = True
    # CREATE FOLDER TRAIN
    creatDir('train')
    # PRINT ASK
    print("Qual o seu nome?")
    # GET NAME
    name = input()
    # SET GLOBAL NAME
    lastName = name
    # CREATE PERSON DIR
    creatDir(name,'train')


def saveImg(img):
    # GET GLOBALS
    global lastName
    # GET ITENS LEN OF TRAIN FOLDER
    qtd = os.listdir(f'train/{lastName}')
    # SAVE IMAGE
    cv2.imwrite(f'train/{lastName}/{str(len(qtd))}.jpg', img)

def trainData():
    # GET GLOBALS
    global recognizer
    global trained
    global persons
    # SET TRAINED TRUE
    trained = True
    # SET PERSONS LIST
    persons = os.listdir('train')
    # ID OF EACH IMAGE
    ids = []
    # NUMPY IMAGE GRAY
    faces = []
    # RUN ALL PERSONS IN TRAIN FOLDER WITH INDEX
    for i,p in enumerate(persons):
        # INCREMENT 1 IN INDEX, I = PERSON ID
        i += 1
        # RUN PERSONS FOLDER, GET ALL 50 IMAGES
        for f in os.listdir(f'train/{p}'):
            # GET IMAGE IN GRAYSCALE
            img = cv2.imread(f'train/{p}/{f}',0)
            # APPEND IMAGE TO FACES LIST
            faces.append(img)
            # APPEND ID TO IDS LIST
            ids.append(i)
    # TRAIN RECOGNIZER
    recognizer.train(faces, np.array(ids))

# LAST NAME
lastName = ''

# SAVE FACE BOOL
saveface = False
savefaceC = 0

# TRAINED
trained = False
persons = []

# READ VIDEO
cap = cv2.VideoCapture(0)

# LOAD HAAR CASCADE CLASSIFIER
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# LOAD RECOGNIZER pip install opencv_contrib_python
recognizer = cv2.face.LBPHFaceRecognizer_create()

# LOOP
while(True):
    
    # READ FRAME
    _, frame = cap.read()

    # GRAY FRAME
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # DETECT FACES IN FRAME
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # RUN ALL FACES IN FRAME
    for i, (x,y,w,h) in enumerate(faces):

        # DRAW RECT IN FACE
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # FACE CROP
        roi_gray = gray[y:y+h, x:x+w]

        # RESIZE FACE CROP TO 50x50
        resize = cv2.resize(roi_gray, (50, 50)) 

        # CHECK IF RECOGNIZER IS TRAINED
        if trained:
            # PREDICT THE FACE
            idf, conf = recognizer.predict(resize)

            # GET PERSON NAME
            nameP = persons[idf-1]
            # IF CONFIDENCI IS LESS THEN 100 PRINT GREEN NAME
            if conf < 100:
                cv2.putText(frame,nameP,(x+5,y+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,0),1,cv2.LINE_AA)
            # IF CONFIDENCI IS MORE THEN 100 PRINT RED NAME
            else:
                cv2.putText(frame,nameP,(x+5,y+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1,cv2.LINE_AA)

            # DRAW TEXT IF IS TRAINED OR NOT
            cv2.putText(frame,'TRAINED',(10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0),1,cv2.LINE_AA)
        else:
            cv2.putText(frame,'NOT TRAINED',(10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1,cv2.LINE_AA)
            
        # IF SAVE IS PRESSED
        if saveface:
            # DRAW TEXT OF SAVE ID
            cv2.putText(frame,str(savefaceC),(10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,255),1,cv2.LINE_AA)
            # INCREMENT ID
            savefaceC += 1
            # SAVE FACE
            saveImg(resize)
        # IF 50 IMAGES STOP
        if savefaceC > 50:
            # RETURN COUNT TO 0
            savefaceC = 0
            # DISABLE SAVE BOOL
            saveface = False


    # DRAW TEXT
    cv2.putText(frame,'Press Space to save face',(10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),1,cv2.LINE_AA)

    # SHOW FRAME
    cv2.imshow('frame',frame)

    # WAITKEY
    key = cv2.waitKey(15)

    # PRESS T TO TRAIN
    if key == 116:
        trainData()

    # PRESS SPACE TO SAVE
    if key == 32:
        saveFace()

    # STOP LOOP
    if key & 0xFF == ord('q'):
        break
        

# RELEASE CAP
cap.release()

# DESTROY ALL WINDOWS
cv2.destroyAllWindows()
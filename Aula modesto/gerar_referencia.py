from cvzone.HandTrackingModule import HandDetector

import cvzone
import cv2
import pickle
import numpy as np
import math


class DragRect():
    def __init__(self, posCenter, colorR, angle, size=[100, 200]):
        self.posCenter = posCenter
        self.size = size
        self.color = colorR
        self.angle = angle

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and \
                cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor

    def angle_update(self, rotation):
        self.angle = rotation


    def color_update(self, wright):
        self.colorR = (wright, 0, 0)


    def resize(self, newH, newW):
        self.size = [newH, newW]

    def check_right_or_wrong(self, imgPro):
        self.spaceCounter = 0

        for pos in imgPro:
            w, h = self.size
            x, y = self.posCenter

            imgCrop = imgPro[y:y + h, x:x + w]
            # cv2.imshow(str(x * y), imgCrop)
            count = cv2.countNonZero(imgCrop)
            number_of_white_pix = np.sum(imgCrop == 255)
            number_of_black_pix = np.sum(imgCrop == 0)
            # print(count, number_of_black_pix, number_of_white_pix)
            # print(self.size, imgCrop.size)

            if count <= 3100:
                self.color = 2
                # self.color = (255, 0, 0)
                # self.thickness = 0
                # self.spaceCounter += 1
                # print("certo")



            else:
                self.color = 1
                # self.color = (0, 0, 255)
                # self.thickness = 0
                # print("errado")
        return self.color

            # cv2.rectangle(pos, self.posCenter, (self.posCenter[0] + w, self.posCenter[1] + h), self.color, self.thickness)
            # cvzone.putTextRect(self, str(count), (x, y + h - 3), scale=1,
            #                    thickness=2, offset=0, colorR=self.color)

        # cvzone.putTextRect(imgPro, f'Free: {spaceCounter}/{len(imgPro)}', (100, 50), scale=3,
        #                    thickness=5, offset=20, colorR=(0, 200, 0))


def detect_object(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 25, 16) #cv2.THRESH_BINARY_INV
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    #Sobel test
    window_name = ('Sobel Demo - Simple Edge Detector')
    scale = 1
    delta = 0
    ddepth = cv2.CV_16S

    grad_x = cv2.Sobel(imgGray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    # Gradient-Y
    # grad_y = cv.Scharr(gray,ddepth,0,1)
    grad_y = cv2.Sobel(imgGray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    t, teste = cv2.threshold(imgBlur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return imgDilate, imgThreshold, teste, grad

# Inicio


#ip = "192.168.200.105:8080"

cap = cv2.VideoCapture(0)
ip = "https://192.168.200.105:8080/video"
#cap.open(ip)
#cap.set(3, 1320) #3, 680
#cap.set(4, 1320) #4,680
# Nomear a janela da câmera
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

# Definir as dimensões desejadas para a janela
largura_janela = 1320
altura_janela = 600

# Redimensionar a janela
cv2.resizeWindow('Image', largura_janela, altura_janela)

detector = HandDetector(detectionCon=0.5)
startDist = None
scale = 0
cx, cy = 150, 150
# colorR = (255, 0, 255)
colorR = (0, 0, 255)
rotation = 0


rectList = []
for x in range(1):
    rectList.append(DragRect([x * 250 + 150, 150], colorR, rotation))

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, flipType=True)


    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)

        # length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[4][0:2], img)
        length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[12][0:2], img)
        # length2, info2, img2 = detector.findDistance(lmList1[8][0:2], lmList1[4][0:2], img)

        if length < 60:
            cursor = lmList1[8][0:2]  # index finger tip landmark
            # call the update here
            for rect in rectList:
                rect.update(cursor)

        # Calcular a distância da mão em relação à câmera

        # Find Function
        # x is the raw distance y is the value in cm
        x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
        y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
        coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C

        lmList1 = hands[0]["lmList"]  # List of 21 Landmark points
        x, y, w, h =hand1["bbox"]
        x1, y1 = lmList1[8][0:2]
        x2, y2 = lmList1[12][0:2]

        distancia = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
        A, B, C = coff
        distanceCM = A * distancia ** 2 + B * distancia + C

        # print(distanceCM, distance)

        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
        # cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x, y))

        # Exibir a distância na janela
        cv2.putText(img, f"Distancia da mao: {distancia}cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


    if len(hands) == 2:
        # print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1]))
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and \
                detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            # print("Zoom Gesture")
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            # point 8 is the tip of the index finger
            if startDist is None:
                # length2, info, img = detector.findDistance(lmList1[8][0:2], lmList2[4][0:2], img)
                # length2, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)

                startDist = length

            # length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[4][0:2], img)
            # length2, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)

            scale = int((length - startDist) // 2)
            print(scale)

    else:
        startDist = None


    # Draw solid
    imgNew = np.zeros_like(img, np.uint8)
    thickness = 3
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size

        # Calcular os vértices do retângulo
        vertices = np.array([(cx - w // 2, cy - h // 2), (cx + w // 2, cy - h // 2), (cx + w // 2, cy + h // 2),
                             (cx - w // 2, cy + h // 2)])

        # Calcular o ângulo atual do retângulo
        retangulo_rotacionado = cv2.minAreaRect(vertices)
        # angulo_atual = retangulo_rotacionado[-1]

        # angulo_desejado = 90
        aux_angulo = retangulo_rotacionado[-1]

        print(scale)
        if scale < 45:
            angulo_desejado = 45
            # Calcular a matriz de rotação para o ângulo desejado
            matriz_rotacao = cv2.getRotationMatrix2D((cx, cy), angulo_desejado, 1.0)
            # print(angulo_desejado)
            if scale > 45:
                angulo_desejado = 120
                # Calcular a matriz de rotação para o ângulo desejado
                matriz_rotacao = cv2.getRotationMatrix2D((cx, cy), angulo_desejado, 1.0)
                # print(angulo_desejado)

        else:
            angulo_desejado = 90
            matriz_rotacao = cv2.getRotationMatrix2D((cx, cy), angulo_desejado, 1.0)

        # Aplicar a matriz de rotação aos vértices do retângulo
        vertices_rotacionados = cv2.transform(np.array([vertices]), matriz_rotacao)[0]

        # Desenhar o retângulo rotacionado em uma imagem
        imagem = np.zeros((400, 400, 3), dtype=np.uint8)

        # chek empty or not empty
        img_dilate, img_threshold, otsu, sobel = detect_object(img)
        color = rect.check_right_or_wrong(img_dilate)
        if color == 1:
            colorR = (255, 0, 0)
        else:
            colorR = (0, 0, 255)

        cv2.drawContours(img, [vertices_rotacionados.astype(int)], 0, (colorR), thickness)
        # angulo_atual = angulo_desejado
        # cvzone.cornerRect(img, (cx - w // 2, cy - h // 2, w, h), 20, rt=1, colorC=(0, 0, 255))

    # #chek empty or not empty
    #
    # img_dilate, img_threshold, otsu, sobel = detect_object(img)
    # for rect in rectList:
    #     color = rect.check_right_or_wrong(img_dilate)

    # teste = cvzone.stackImages([img, img_dilate, otsu], 3, 0.5)
    # teste = cvzone.stackImages([img], 1, 1)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break






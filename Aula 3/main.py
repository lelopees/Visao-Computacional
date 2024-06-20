# -*- coding: utf-8 -*-
import cv2 
from unidecode import unidecode

img = cv2.imread('8_t3.jpg')

# desenhar uma linha 
# aqui as cores são bgr
#cv2.line(img,(10,10), (200,200), (255,0,0), 10)

# desenhar retangulo
# onde começa o retangulo | 
#cv2.rectangle(img, (10,10), (200,200), (255,0,0), 10)

#print(img.shape)
 
#500 = comprimento
#75 = largura
x,y,w,h = 0,0,img.shape[1],75

        # Draw black background rectangle
cv2.rectangle(img, (x, x), (w, h), (0,0,0), -1)

# desenhar circulo
#cv2.circle(img, (150,30), 50, (0,0,255), 3)

# desenhar texto 

img1 = img

text = "Imagem Invalida, tire uma nova foto."  
 
cv2.putText(img1, text,
        (10, 20),
        cv2.QT_FONT_NORMAL,
        0.5,
        ( 0, 255, 0), 
        1, cv2.LINE_AA)
cv2.imshow('img1', img1)
 
cv2.putText(img, text,
        (10, 20),
        cv2.QT_FONT_NORMAL,
        0.5,
        ( 0, 255, 0), 
        1)
cv2.imshow('img', img)
 


cv2.waitKey(0)
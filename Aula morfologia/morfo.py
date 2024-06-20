import cv2
import numpy as np

img = cv2.imread('8_t3.jpg')

cv2.imshow('img', img)

t, data_1 = cv2.threshold(img,90,255,cv2.THRESH_BINARY)
print(t)
_, data_2 = cv2.threshold(img,95,255,cv2.THRESH_BINARY)
_, data_3 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
_, data_4 = cv2.threshold(img,105,255,cv2.THRESH_BINARY)

cv2.imshow('data_1', data_1)
cv2.imshow('data_2', data_2)
cv2.imshow('data_3', data_3)
cv2.imshow('data_4', data_4)

img = data_1

# Define standard colors
colors = np.array([(255, 255, 255), (0, 0, 255)])  # black, white, red
#print(colors[:, None, None])
# Map the colors in the image using numpy broadcasting
# np.linalg.norm calcula a norma euclidiana
distances = np.linalg.norm(img - colors[:, None, None], axis=3)
#print(distances)



""""
#### Define standard colors
img = data_1

# Define standard colors
colors = np.array([(255, 255, 255), (0, 0, 255)])  # black, white, red

# Map the colors in the image using numpy broadcasting
# np.linalg.norm calcula a norma euclidiana
distances = np.linalg.norm(img - colors[:, None, None], axis=3)
print(distances)

# retorna um array com os indice minimos de cada matriz. 
# Cada elemento do array argmin_indices será o índice da cor de referencia mais proxima para cada pixel da imagem
# Axis 0 = representa eixo vertical

#a linha argmin_indices = np.argmin(distances, axis=0)
#encontra os índices das cores de referência mais próximas para cada pixel da imagem,
#com base nas distâncias calculadas anteriormente

argmin_indices = np.argmin(distances, axis=0)
img = colors[argmin_indices]
img = cv2.convertScaleAbs(img) ## Corrigindo formato
    
mask_2=np.ones((2,1),np.uint8)
data=cv2.morphologyEx(img,cv2.MORPH_OPEN,mask_2)
cv2.imshow('data', data)
"""
cv2.waitKey(0)
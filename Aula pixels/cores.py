import cv2
import numpy as np

# Carregue a imagem
imagem = cv2.imread('IN-2LG.jpg')

# Ajuste de brilho
brilho = 1.2
imagem_ajustada = np.clip(imagem * brilho, 0, 255).astype(np.uint8)

# Ajuste de contraste
contraste = 1.5
imagem_ajustada = np.clip((imagem_ajustada - 127) * contraste + 127, 0, 255).astype(np.uint8)

# Ajuste de saturação
saturacao = 1.2
imagem_hsv = cv2.cvtColor(imagem_ajustada, cv2.COLOR_BGR2HSV)
imagem_hsv[:,:,1] = np.clip(imagem_hsv[:,:,1] * saturacao, 0, 255).astype(np.uint8)
imagem_ajustada = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR)

# Exibir a imagem original e a imagem ajustada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Ajustada', imagem_ajustada)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

def retinex_single_scale(image, sigma):
    # Aplicando um filtro Gaussiano na imagem original
    blurred = cv2.GaussianBlur(image, (0, 0), sigma)

    # Calculando o logaritmo da imagem original e da imagem filtrada
    image_log = np.log(image.astype(np.float32) + 1)
    blurred_log = np.log(blurred.astype(np.float32) + 1)

    # Subtraindo o logaritmo da imagem filtrada do logaritmo da imagem original
    result = image_log - blurred_log

    # Convertendo a imagem de volta para o intervalo de 0 a 255
    result = np.clip(result, 0, 255)
    result = (result / np.max(result)) * 255
    result = result.astype(np.uint8)

    return result

# Carregando a imagem
imagem = cv2.imread('IN-2LG.jpg')

# Convertendo a imagem para escala de cinza
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicando a função Retinex Single Scale
imagem_retinex = retinex_single_scale(imagem_gray, sigma=10)

# Exibindo a imagem original e a imagem processada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Retinex', imagem_retinex)
cv2.waitKey(0)
cv2.destroyAllWindows()

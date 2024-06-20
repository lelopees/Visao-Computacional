import numpy as np
import cv2
import time
from tqdm import tqdm

ESCAPE_KEY_ASCII = 27

def onChange(value):
    #print('valor alterado', value)
    pass

img = cv2.imread('Orange.png')
copyimg = img.copy()

windowTitle = "Ajuste de Brilho e Contraste"
cv2.namedWindow(windowTitle)

cv2.createTrackbar("contraste", windowTitle, 100, 100, onChange)
cv2.createTrackbar("brilho", windowTitle, 0, 200, onChange)

before_contrast = 100
update_contrast = False

before_brigthness = 0
update_brigthness = False

counter_time = 0

while True:
 
    current_contrast = cv2.getTrackbarPos("contraste", windowTitle)
    current_brigthness = cv2.getTrackbarPos("brilho", windowTitle)
    
    # valor de contraste do trackbar foi alterado pelo usuário
    if before_contrast != current_contrast:
        update_contrast = True
        counter_time = time.time()
        before_contrast = current_contrast

    # valor de brilho do trackbar foi alterado pelo usuário
    if before_brigthness != current_brigthness:
        update_brigthness = True
        counter_time = time.time()
        before_brigthness = current_brigthness

    # se tiver passado 1 segundo desde que o usuário mexeu no trackbar
    if time.time() - counter_time > 1:
        # se tiver sido marcado que é pra atualizar contraste ou brilho
        if update_contrast == True or update_brigthness == True:
            '''
            # atualizamos o contraste da imagem
            copyimg = img.copy()

            height, width, channels = img.shape
            
            # para cada informação de cor, de cada pixel, atualizamos o contraste
            for y in tqdm(range(height)):
                for x in range(width):
                    for c in range(channels):
                        newColorValue = copyimg[y][x][c] * (current_contrast / 100) + current_brigthness
                        # se ultrapassar os valores de 0 a 255 o np força ser esse valor
                        copyimg[y][x][c] = np.clip(newColorValue, 0, 255)
            '''
    

            copyimg = cv2.convertScaleAbs(img, alpha=current_contrast / 100, beta = current_brigthness)
            update_contrast = False
            update_brigthness = False
    cv2.imshow(windowTitle, copyimg)

    #print(contrast_value)

    keyPressed = cv2.waitKey(1) & 0xFF

    if keyPressed == ESCAPE_KEY_ASCII:
        break

cv2.destroyAllWindows()
import cv2
import numpy as np

# funcoes
def nothing(x):
    pass

# criar de janeka de trackbars
cv2.namedWindow('trackbars')

# criar as trackbars

#trackbar_name: É o nome da trackbar.
#window_name: É o nome da janela onde a trackbar será exibida.
#start_value: É o valor inicial da trackbar.
#max_value: É o valor máximo que a trackbar pode atingir.
#callback: É uma função de retorno de chamada que será chamada sempre 
#que o valor da trackbar for alterado pelo usuário. Essa função é opcional.

cv2.createTrackbar('l-h', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('l-s', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('l-v', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('u-h', 'trackbars', 255, 255, nothing)
cv2.createTrackbar('u-s', 'trackbars', 255, 255, nothing)
cv2.createTrackbar('u-v', 'trackbars', 255, 255, nothing)

# capturar video
cap = cv2.VideoCapture(0)

while True:

    #recuperar trackbar
    lh =cv2.getTrackbarPos('l-h', 'trackbars')
    ls =cv2.getTrackbarPos('l-s', 'trackbars')
    lv =cv2.getTrackbarPos('l-v', 'trackbars')
    uh =cv2.getTrackbarPos('u-h', 'trackbars')
    us =  cv2.getTrackbarPos('u-s', 'trackbars')
    uv =  cv2.getTrackbarPos('u-v', 'trackbars')

    #recuperar frame do video
    ret, frame = cap.read()    

    # criar lower e upper
    lowwer = np.array([lh,ls,lv])
    upper = np.array([uh,us,uv])

    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    # criar mascara
    mask = cv2.inRange(hsv, lowwer, upper)

    # unir a mascara
    result = cv2.bitwise_and(frame, frame,  mask=mask)

    # exibindo a mascara
    cv2.imshow('mask', mask)

    # exibindo a mascara
    cv2.imshow('result', result)

    # exibindo o frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# libero o cap
cap.release()

# destruo todas as janelas
cv2.destroyAllWindows() 



import cv2


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

cv2.createTrackbar('x', 'trackbars', 0, 800, nothing)
cv2.createTrackbar('y', 'trackbars', 0, 800, nothing)
cv2.createTrackbar('w', 'trackbars', 100, 800, nothing)
cv2.createTrackbar('h', 'trackbars', 100, 800, nothing)

# capturar video
cap = cv2.VideoCapture(0)

while True:

    #recuperar trackbar
    x =cv2.getTrackbarPos('x', 'trackbars')
    y =cv2.getTrackbarPos('y', 'trackbars')
    w =cv2.getTrackbarPos('w', 'trackbars')
    h =cv2.getTrackbarPos('h', 'trackbars')

    #recuperar frame do video
    ret, frame = cap.read()

    roi = frame[y:h, x:w]
    
    cv2.imshow('roi', roi) 

    # exibindo o frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# libero o cap
cap.release()

# destruo todas as janelas
cv2.destroyAllWindows() 



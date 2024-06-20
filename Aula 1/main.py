# IMPORTS
import cv2

# READ IMAGE
img = cv2.imread('Orange.png')

# SHOW IMAGE
#cv2.imshow('img', img) 

# salvar imagem
cv2.imwrite('nova.png', img)

# roi = região de interesse
roi = img[75:250, 100:300]
cv2.imshow('roi', roi) 


# imagem redimensionada
img_resize = cv2.resize(img, (600,600))
cv2.imshow('resize', img_resize)


# WAIT KEY
cv2.waitKey(0)
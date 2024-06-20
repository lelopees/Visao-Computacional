import cv2

url = '15_t3.jpg'

imagem = cv2.imread(url)
imagemColorida = imagem

#imagemColorida = cv2.resize(imagem, (0,0), fx=0.2, fy=0.2)
imagemCinza = cv2.cvtColor(imagemColorida, cv2.COLOR_BGR2GRAY)

imagemLaplacian = cv2.Laplacian(imagemCinza, cv2.CV_8U)
# imagem 
imagemSub = cv2.subtract(imagemLaplacian,imagemCinza)
imagemSub2 = cv2.subtract(imagemCinza,imagemLaplacian)

 


cv2.imshow('TelaColorida', imagemColorida)
#cv2.imshow('TelaCinza', imagemCinza)
cv2.imshow('TelaRealceBordas', imagemLaplacian)
cv2.imshow('TelaSub', imagemSub)
cv2.imshow('TelaSub2', imagemSub2)

 

cv2.waitKey(0)

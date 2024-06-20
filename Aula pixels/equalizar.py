import cv2

img = cv2.imread('IN-2LG.jpg')
imagem_cinza1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
histeq=cv2.equalizeHist(imagem_cinza1)
cv2.imwrite('histeqg_py.png',histeq)
cv2.imwrite('imagem_cinza1.png',imagem_cinza1)

cv2.waitKey(0)
cv2.destroyAllWindows()

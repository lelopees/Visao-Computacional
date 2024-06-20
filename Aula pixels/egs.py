import cv2
import numpy as np 

# Caminho para a imagem que você quer abrir 
mask_egs = cv2.imread('1709571059639.jpg')
original = cv2.imread('1709571672439.jpg')
cv2.imwrite('mask_egs.png', mask_egs)
cv2.imwrite('original_egs.png', original)

print('ENCONTROU EGS')
hh, ww = mask_egs.shape[:2]    

cv2.cvtColor(mask_egs, cv2.COLOR_RGB2GRAY)

#### Máscara EGS real 
gs_image = cv2.bitwise_and(original, original, mask_egs)
gs_image[mask_egs==0] = [0,0,0]
        
#####################################################
##  Estimando EGS
# get the single external contours
contours = cv2.findContours(mask_egs, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
big_contour = max(contours, key=cv2.contourArea)

# get rotated rectangle from contour
# get its dimensions
# get angle relative to horizontal from rotated rectangle
rotrect = cv2.minAreaRect(big_contour)
(center), (width,height), angle = rotrect
box = cv2.boxPoints(rotrect)
boxpts = np.intp(box)

 # Calcula o centro da imagem
centro_imagem = (ww // 2, hh // 2)

# Calcula a posição horizontal do centro do retângulo em relação ao centro da imagem
posicao_horizontal_EGS = center[0] - centro_imagem[0]
#organizando angulo, dependendo da posição da figura, esquerda ou direita
#print('Angle: ', angle)
if angle < -45 and width > height:
    angle = -(90 + angle)
# otherwise, check width vs height
else:
    if angle > -45 and width > height:
        angle = -(-90 +angle)
    else:
        angle= -angle
 
# negate the angle to unrotate
neg_angle = -angle 
# Get rotation matrix
M = cv2.getRotationMatrix2D(center, neg_angle, scale=1.0)
# unrotate to rectify 
rectified = cv2.warpAffine(mask_egs, M, (ww, hh), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# threshold it again to binary
rectified = cv2.threshold(rectified, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# get bounding box of contour of rectified image
cntrs = cv2.findContours(rectified, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#print('contoro',cntrs)
cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]
###### Desse modo quando tiver dois desenhos seleciono o maior
cntr = max(contours, key=cv2.contourArea)
x,y,w,h = cv2.boundingRect(cntr)

# crop to blob limits
crop_egs = rectified[y:y+h, x:x+w] 

# get width at every row of crop
count = np.count_nonzero(crop_egs, axis=1)
#### Calculando porção média da egs 30%
total = 0
for i in range(int(h*0.30-h*0.10)):
    total = total + count[i]

media=(total)/(int(h*0.30-h*0.10))

"""
###<- média de pixels _ regra de três
egs_dimens = (media * 20) / w_chav
egs_dimens = math.floor(egs_dimens)
"""


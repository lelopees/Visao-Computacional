# -*- coding: utf-8 -*-
import cv2 

#img = cv2.imread('usar.png')
#print(img.shape) 
#img = cv2.imread('imagem_segmentada12.jpeg')
img = cv2.imread('imagem1206.jpeg')

print(img.shape) 
img_espelhada = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#img = cv2.resize(img, (600, 875))

print(img.shape) 

print(img.shape[1])
x,y,w,h =  0,0,375,75

        # Draw black background rectangle
#cv2.rectangle(img, (x, x), (w, h), (0,0,0), -1) 


        # Load image, define rectangle bounds
#x,y,w,h = 0,0,img.shape[1],75 

        # Draw black background rectangle
#img
total_f_m = 315
total_conac = 800 + total_f_m
print(total_conac)

h_pos = int(215/2)
h_off = 36#int(h_pos/2) - 10
w_posicao = 375
w_off= int(w_posicao/4) # soma da largura cor carne + cor gordura
#w_off = int(w_off_soma/2) 
print(w_off) 

#img[(h_pos - 15):215, 0:(350)] = (255, 0, 255)

#img[43:43+15, 53:80] = (255, 0, 255)
# cor de carne
#img[h_off:h_off+16, w_off-10:w_off+25] = (0, 0, 0)
# cor da corgura
#img[h_off:h_off+16, int(w_posicao-w_off)-10:int(w_posicao-w_off)+25] = (0, 0, 0)
#cv2.rectangle(img, (0, 186), (374, 90), (0,255,0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
font_thickness = 1
font_color = (255, 255, 255)
line_type = cv2.LINE_AA             
    
    # adiciona texto conforme as posições e parametros das categorias
dados_texto = []

"""

cv2.putText(img, "OFF",
        (w_off - 10, h_off + 13),
        cv2.QT_FONT_NORMAL,
        0.6,
        ( 255, 255, 255), 
        1, cv2.LINE_AA)

cv2.putText(img, "OFF",
        (int(w_posicao-w_off) - 10, h_off + 13),
        cv2.QT_FONT_NORMAL,
        0.6,
        ( 255, 255, 0), 
        1, cv2.LINE_AA)



"""

posicao_padrao = [(10, h_pos + 25), (10, ( h_pos + 15) + 40), (10, (h_pos + 15) + 70), (200, h_pos + 25), (200, ( h_pos + 15) + 40)]

categoria_global = ["marbling", "loinEyeArea", "fatThickness", "meatColor", "fatColor"]
    #print(payloadByte)
BeefArea = 10
marble = 660
egs_dimens = 14 
cor_carne = "B2"
cor_gord = "A5"
    
for i, variavel in enumerate(categoria_global): 
        posicao = posicao_padrao[i]
        if variavel == 'loinEyeArea':
                texto = "AOL = {:.1f} cm2".format(BeefArea)
        elif variavel == 'marbling':
                texto = "Marmoreio = {:.0f}".format(marble)
        elif variavel == 'fatThickness':
                texto = "EGS = {:.1f} mm".format(egs_dimens)
        elif variavel == 'meatColor':
                texto = "Cor Carne Ø = " + str(cor_carne)
        elif variavel == 'fatColor':
                texto = "Cor Gordura ø = " + format(str(cor_gord))

        dados_texto.append((texto, posicao))     
    
        #for texto, posicao in dados_texto:
             #   cv2.putText(img, texto, posicao, font, font_scale, font_color, font_thickness, line_type)

#cv2.imwrite('imagem_modificada.png', img)
cv2.imwrite('imagemerrada1206.jpeg', img_espelhada)
cv2.imshow('img', img)
#cv2.imshow('img2', img_espelhada)
#vazio_redimensionado = cv2.resize(vazio, (30, 30))


x_inicio = 0
y_inicio = 0

"""
#cv2.putText(img, "Testando ø",
        (10, 10),
        cv2.QT_FONT_NORMAL,
        0.5,
        ( 255, 255, 255), 
        1, cv2.LINE_AA)

        """

# Copiar a região do vazio para a img
#img[y_inicio:y_inicio+vazio_redimensionado.shape[0], x_inicio:x_inicio+vazio_redimensionado.shape[1]] = vazio_redimensionado

#cv2.imshow('vazio', vazio_redimensionado) 



"""

text = "Imagem Invalida, tire uma nova foto."  

cv2.putText(img, text,
        (10, 120),
        cv2.QT_FONT_NORMAL,
        0.5,
        ( 255, 255, 255), 
        1, cv2.LINE_AA)
padding_top = 0
padding_bottom = 0
padding_left = 390
padding_right = 390

# Aplica o padding na imagem
img_padded = cv2.copyMakeBorder(img, padding_top, padding_bottom, padding_left, padding_right, cv2.BORDER_CONSTANT, value=(0, 0, 0))

cv2.putText(img_padded, text,
        (10, 20),
        cv2.QT_FONT_NORMAL,
        0.5,
        (255, 255, 255), 
        1, cv2.LINE_AA) 
 

cv2.imshow('img_padded', img_padded)


padding_top = 75
padding_bottom = 0
padding_left = 0
padding_right = 0

# Aplica o padding na imagem
img_padded2 = cv2.copyMakeBorder(img, padding_top, padding_bottom, padding_left, padding_right, cv2.BORDER_CONSTANT, value=(0, 0, 0))


cv2.putText(img_padded2, text,
        (10, 20),
        cv2.QT_FONT_NORMAL,
        0.5,
        ( 255, 255, 255), 
        1, cv2.LINE_AA)
cv2.imshow('img_padded2', img_padded2) 
 

cv2.imshow('img_padded', img_padded)

"""
cv2.waitKey(0)
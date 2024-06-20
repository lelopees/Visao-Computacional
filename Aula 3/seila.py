import cv2
import numpy as np  

img2 = cv2.imread('vai0506.jpeg') 
cv2.imshow('Imagem com Texto Centralizado',img2 )

sId = 1
sLote = 969 

fonte = cv2.QT_FONT_NORMAL
escala = 0.6
cor =  (0, 180, 180)  # Cor do texto em BGR (branco)
espessura = 1

# Obtém as dimensões do texto a ser exibido
texto_sid = f'ID: {sId}'
texto_slote = f'Lote: {sLote}'
(_, altura), _ = cv2.getTextSize(texto_sid, fonte, escala, espessura)

# Coloca o texto na imagem
posicao = (10, img2.shape[0] - 10 - altura)  # 10 pixels a partir da borda inferior e 10 pixels da borda esquerda
cv2.putText(img2, texto_sid, posicao, fonte, escala, cor, espessura)
posicao = (10, img2.shape[0] - 5)  # Aumenta a altura para colocar o texto do lote abaixo do texto do sId
cv2.putText(img2, texto_slote, posicao, fonte, escala, cor, espessura)

# Exibe a imagem com o texto adicionado
cv2.imshow('Imagem com Texto Centralizado', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

#contours = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

"""


dest_or = cv2.bitwise_or(img2, img1, mask = None)

cv2.imshow('Imagem com Texto Centralizado',dest_or )
texto = "OFF"
font = cv2.QT_FONT_NORMAL
escala = 2
espessura = 3
    #cor_texto = (255, 255, 255) 
   
font_color = (0, 255, 255)
font_scale = 1.4
line_type = cv2.LINE_AA      
blank_image_meat = np.zeros((400,400,3), np.uint8) ## Quadro preto        
altura, largura, _ = blank_image_meat.shape    

blank_image_meat[:,0:400] = (217,217,217) 

(tamanho_texto, _), _ = cv2.getTextSize(texto, font, escala, espessura) 
posicao = [int((largura - tamanho_texto) / 2), int(altura / 4)]
print(posicao)
posicao[0] = posicao[0]+15
posicao[1] = posicao[1]+10
print(posicao)
         # Cor do texto (branco)
       # print(posicao)
       # blank_image_meat[posicao[1]-45:posicao[1]+5, posicao[0]:posicao[0]+120] = (0,0,0)
cv2.putText(blank_image_meat, texto, posicao, font, font_scale, (82,82,82), 2, line_type)  

blank_image_meat[altura//2:, :] = 0 


saida = img
height, width, _ = saida.shape 

padding_top = 75
padding_bottom = 0
padding_left = 0
padding_right = 0        
    
font = cv2.FONT_ITALIC
fontScale = 0.8
text = "Erro na imagem. Tire uma nova foto."
fontColor = (255, 255, 255)
lineType = 2
text_size, _ = cv2.getTextSize(text, font, fontScale, lineType)
text_width = text_size[0]
text_height = text_size[1] 
        
x = int((width - padding_left - padding_right) / 2)  - int(text_width / 2)
y =  int(padding_top + (padding_bottom - padding_top + 16) / 2)    

        
#x = start_x - int(text_width / 2)
#y = start_y        
        
bottomLeftCornerOfText = (x, y)
        
saida = cv2.copyMakeBorder(saida, padding_top, padding_bottom, padding_left, padding_right, cv2.BORDER_CONSTANT, value=(0, 0, 255))        

        
cv2.putText(saida, text,bottomLeftCornerOfText,font,fontScale,fontColor, lineType, cv2.LINE_AA)

"""


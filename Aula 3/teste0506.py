import cv2
import numpy as np

# Carrega a imagem
#imagem = cv2.imread("8_t3.jpg")
blank_image_fat = np.zeros((500,600,3), np.uint8) 
blank_image_fat[:,0:600] = (217,217,217)           
# Obtém as dimensões da imagem
altura, largura, _ = blank_image_fat.shape
k = altura//2
# Define a metade superior da imagem como preta
blank_image_fat[k:, :, :] = 0 
 
texto = "OFF"
fonte = cv2.QT_FONT_NORMAL
escala = 2
espessura = 3
# Calcula a posição do texto para centralizá-lo na metade de cima da parte preta
(tamanho_texto, _), _ = cv2.getTextSize(texto, fonte, escala, espessura)
posicao = (int((largura - tamanho_texto) / 2)+15, int(altura / 4))
cor_texto = (255, 255, 255)  # Cor do texto (preto)
print(posicao)
#blank_image_fat[posicao[1]-45:posicao[1]+5, posicao[0]:posicao[0]+120] = (0,0,0)
cv2.putText(blank_image_fat, texto, posicao, fonte, 1.3, (82,82,82), 2, cv2.LINE_AA)

dados_texto = []
categoria_global = ["marbling", "loinEyeArea", "fatThickness", "meatColor", "fatColor"]

"""
 for i, variavel in enumerate(categoria_global): 
        posicao = posicao_padrao[i]
        if variavel == 'loinEyeArea':
            texto = "AOL = {:.1f} cm2".format(BeefArea)
        elif variavel == 'marbling':
            texto = "Marmoreio = {:.0f}".format(marble)
        elif variavel == 'fatThickness':
            texto = "EGS = {:.1f} mm".format(egs_dimens)
        elif variavel == 'meatColor':
            texto = "Cor Carne = " + str(cor_carne)
        elif variavel == 'fatColor':
            texto = "Cor Gordura = " + str(cor_gord)

        dados_texto.append((texto, posicao))     
    
    for texto, posicao in dados_texto:
        cv2.putText(blank_image_fat, texto, posicao, font, font_scale, font_color, font_thickness, line_type)
"""

#font = cv2.FONT_HERSHEY_SIMPLEX
#font_scale = 0.6
#font_thickness = 1
#font_color = (0, 255, 255) # amarelo
#line_type = cv2.LINE_AA       


posicao_padrao = [(10, 250), (10, 315)]
dados_texto = []
categoria_global =  ['marbling', 'loinEyeArea', 'fatThickness', 'fatColor', "meatColor"]
nova_lista = [item for item in categoria_global if item == 'fatColor' or item == 'meatColor']

print(nova_lista)
cor_carne = 'D3'
cor_gord = "A2"


for i, variavel in enumerate(nova_lista): 
        posicao = posicao_padrao[i]
        if variavel == 'meatColor':
            texto = "Cor Carne = " + str(cor_carne)
        elif variavel == 'fatColor':
            texto = "Cor Gordura = " + str(cor_gord)
        dados_texto.append((texto, posicao))   
for texto, posicao in dados_texto:
        cv2.putText(blank_image_fat, texto, posicao, cv2.QT_FONT_NORMAL, 1.3, (0,255,255), 1, cv2.LINE_AA)

print(dados_texto)

#cv2.putText(blank_image_fat, "Marmoreio = ", (20,250), cv2.QT_FONT_NORMAL, 1.2, (0,255,255), 1, cv2.LINE_AA)
#cv2.putText(blank_image_fat, "AOL = ", (20,315), cv2.QT_FONT_NORMAL, 1.2, (0,255,255), 1, cv2.LINE_AA)
#cv2.putText(blank_image_fat, "EGS = ", (20,380), cv2.QT_FONT_NORMAL, 1.2, (0,255,255), 1, cv2.LINE_AA)

#cv2.putText(blank_image_fat, "Marmoreio = ", (20,250), 3, 1, (0,255,255), 1, cv2.LINE_AA)
#cv2.putText(blank_image_fat, "AOL = ", (20,250), 3, 1, (0,255,255), 1, cv2.LINE_AA)
#cv2.putText(blank_image_fat, "EGS = ", (20,250), 3, 1, (0,255,255), 1, cv2.LINE_AA)

print(posicao[0])

#blank_image_fat[posicao[0]:posicao[0]+10, posicao[1]:posicao[1]:10] = (0,255,255)

#blank_image_fat[posicao[1]-40:130, 150:170] = (0,0,255)

# Exibe a imagem modificada
#cv2.imshow("Imagem Preta", imagem)
cv2.imshow("Imagem blank_image_fat", blank_image_fat)
cv2.waitKey(0)
cv2.destroyAllWindows()

from PIL import Image
import cv2
import numpy as np

def obter_numero_pixels(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    largura, altura = imagem.size
    return largura * altura

def converter_para_megapixels(numero_pixels):
    return numero_pixels / 1e6

# Exemplo de uso
caminho_imagem1 = "IN-11LG.jpg"
caminho_imagem2 = "IN-11poco.jpg" #pocophone f1 = 12mpx
caminho_imagem3 = "IN_LE.jpg"

imagem1 = cv2.imread(caminho_imagem1)
imagem2 = cv2.imread(caminho_imagem2)
imagem3 = cv2.imread(caminho_imagem3)

imagem_cinza1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
# Calculando o brilho médio
brilho_medio1 = cv2.mean(imagem_cinza1)[0]

imagem_cinza2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY) 
brilho_medio2 = cv2.mean(imagem_cinza2)[0]

imagem_cinza3 = cv2.cvtColor(imagem3, cv2.COLOR_BGR2GRAY) 
brilho_medio3 = cv2.mean(imagem_cinza3)[0]

""""Algoritmo de Estimativa de Iluminação Retinex (Retinex): 
O algoritmo Retinex é uma técnica de processamento de imagem 
que estima a iluminação e a refletância de uma imagem separadamente. 
Ele pode ser usado para analisar o brilho global da imagem, 
considerando a iluminação uniforme.
""" 
brilho_global1 = np.mean(np.log1p(imagem_cinza1)) 
brilho_global2 = np.mean(np.log1p(imagem_cinza2))
brilho_global3 = np.mean(np.log1p(imagem_cinza3))

variancia1 = np.var(imagem1)
variancia2 = np.var(imagem2)
variancia3 = np.var(imagem3)

valor_maximo1 = np.max(imagem1)
valor_minimo1 = np.min(imagem1)
diferenca1 = valor_maximo1 - valor_minimo1

valor_maximo2 = np.max(imagem2)
valor_minimo2 = np.min(imagem2)
diferenca2 = valor_maximo2 - valor_minimo2

valor_maximo3 = np.max(imagem3)
valor_minimo3 = np.min(imagem3)
diferenca3 = valor_maximo3 - valor_minimo3

imagem_hsv1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2HSV)
# Separando os canais de cores HSV
canal_saturacao1 = imagem_hsv1[:, :, 1]

# Calculando a média da saturação
saturacao_media1 = np.mean(canal_saturacao1)

imagem_hsv2= cv2.cvtColor(imagem2, cv2.COLOR_BGR2HSV)
canal_saturacao2 = imagem_hsv2[:, :, 1]
saturacao_media2 = np.mean(canal_saturacao2)

imagem_hsv3= cv2.cvtColor(imagem3, cv2.COLOR_BGR2HSV)
canal_saturacao3 = imagem_hsv3[:, :, 1]
saturacao_media3 = np.mean(canal_saturacao3)

# Aplicando o operador Laplaciano
laplaciano1 = cv2.Laplacian(imagem1, cv2.CV_64F)
# Calculando a medida de nitidez
medida_nitidez1 = np.mean(laplaciano1)

# Aplicando o operador Laplaciano
laplaciano2 = cv2.Laplacian(imagem2, cv2.CV_64F)
# Calculando a medida de nitidez
medida_nitidez2 = np.mean(laplaciano2)

print("Brilho médio da LG:", brilho_global1)
print("Brilho médio da POCO:", brilho_global2)
#print("Brilho médio da LE:", brilho_global3)

print("variancia da LG:", variancia1)
print("variancia da POCO:", variancia2)
#print("variancia da LE:", variancia3)

print("Saturação média da LG:", saturacao_media1)
print("Saturação média da POCO:", saturacao_media2)
#print("Saturação média da LE:", saturacao_media3)

print("Nitidez LG:", medida_nitidez1)
print("Nitidez POCO:", medida_nitidez2)

#print("Contraste da LG (diferença máximo-mínimo):", diferenca1)
#print("Contraste da POCO (diferença máximo-mínimo):", diferenca2)
#print("Contraste da LE (diferença máximo-mínimo):", diferenca3)

numero_pixels_imagem1 = obter_numero_pixels(caminho_imagem1)
numero_pixels_imagem2 = obter_numero_pixels(caminho_imagem2)
#numero_pixels_imagem3 = obter_numero_pixels(caminho_imagem3)

megapixels_imagem1 = converter_para_megapixels(numero_pixels_imagem1) # lg
megapixels_imagem2 = converter_para_megapixels(numero_pixels_imagem2) # pocophone
#megapixels_imagem3 = converter_para_megapixels(numero_pixels_imagem3) # xiomi note pro 8 

print("Imagem LG tem", megapixels_imagem1, "megapixels.")
print("Imagem POCO tem", megapixels_imagem2, "megapixels.")
#print("Imagem LE tem", megapixels_imagem3, "megapixels.") 
"""
print("Imagem 1 tem", numero_pixels_imagem1, "n de pix.")
print("Imagem 2 tem", numero_pixels_imagem2, "n de pix.")
print("Imagem 3 tem", numero_pixels_imagem3, "n de pix.")

"""
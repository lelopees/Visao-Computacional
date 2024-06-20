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
caminho_imagem1 = "foto1.jpg" 

imagem1 = cv2.imread(caminho_imagem1) 

imagem_cinza1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
# Calculando o brilho médio
brilho_medio1 = cv2.mean(imagem_cinza1)[0]
 
""""Algoritmo de Estimativa de Iluminação Retinex (Retinex): 
O algoritmo Retinex é uma técnica de processamento de imagem 
que estima a iluminação e a refletância de uma imagem separadamente. 
Ele pode ser usado para analisar o brilho global da imagem, 
considerando a iluminação uniforme.
""" 
brilho_global1 = np.mean(np.log1p(imagem_cinza1))  

variancia1 = np.var(imagem1) 

valor_maximo1 = np.max(imagem1)
valor_minimo1 = np.min(imagem1)
diferenca1 = valor_maximo1 - valor_minimo1

imagem_hsv1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2HSV)
# Separando os canais de cores HSV
canal_saturacao1 = imagem_hsv1[:, :, 1]

# Calculando a média da saturação
saturacao_media1 = np.mean(canal_saturacao1)

# Aplicando o operador Laplaciano
laplaciano1 = cv2.Laplacian(imagem1, cv2.CV_64F)
# Calculando a medida de nitidez
medida_nitidez1 = np.mean(laplaciano1)

print("Brilho médio da LG:", brilho_global1) 
print("variancia da LG:", variancia1) 
print("Saturação média da LG:", saturacao_media1) 
print("Nitidez LG:", medida_nitidez1) 
 
numero_pixels_imagem1 = obter_numero_pixels(caminho_imagem1) 

megapixels_imagem1 = converter_para_megapixels(numero_pixels_imagem1) # lg 

print("Imagem LG tem", megapixels_imagem1, "megapixels.") 
"""
print("Imagem 1 tem", numero_pixels_imagem1, "n de pix.")
print("Imagem 2 tem", numero_pixels_imagem2, "n de pix.")
print("Imagem 3 tem", numero_pixels_imagem3, "n de pix.")

"""
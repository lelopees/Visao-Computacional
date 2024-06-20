from PIL import Image

def obter_numero_pixels(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    largura, altura = imagem.size
    return largura * altura

def converter_para_megapixels(numero_pixels):
    return numero_pixels / 1e6

# Exemplo de uso
caminho_imagem1 = "IN1LG.jpg"
caminho_imagem2 = "IN1POCO.jpg" #pocophone f1 = 12mpx
caminho_imagem3 = "IN_LE.jpg"

numero_pixels_imagem1 = obter_numero_pixels(caminho_imagem1)
numero_pixels_imagem2 = obter_numero_pixels(caminho_imagem2)
numero_pixels_imagem3 = obter_numero_pixels(caminho_imagem3)

megapixels_imagem1 = converter_para_megapixels(numero_pixels_imagem1) # lg
megapixels_imagem2 = converter_para_megapixels(numero_pixels_imagem2) # pocophone
megapixels_imagem3 = converter_para_megapixels(numero_pixels_imagem3) # xiomi note pro 8
megapixels_imagem4 = converter_para_megapixels(16054528) # foto padrão leticia 3472x4624
megapixels_imagem5 = converter_para_megapixels(64144128) # foto ativo 64 leticia 6936x9248
megapixels_imagem6 = converter_para_megapixels(419200) # foto de saida leticia 800x524

print("Imagem 1 tem", megapixels_imagem1, "megapixels.")
print("Imagem 2 tem", megapixels_imagem2, "megapixels.")
print("Imagem 3 tem", megapixels_imagem3, "megapixels.")
print("Imagem 4 tem", megapixels_imagem4, "megapixels.") 
print("Imagem 5 tem", megapixels_imagem5, "megapixels.") 
print("Imagem 6 tem", megapixels_imagem6, "megapixels.") 

print("Imagem 1 tem", numero_pixels_imagem1, "n de pix.")
print("Imagem 2 tem", numero_pixels_imagem2, "n de pix.")
print("Imagem 3 tem", numero_pixels_imagem3, "n de pix.")
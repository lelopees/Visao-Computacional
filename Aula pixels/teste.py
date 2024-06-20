from PIL import Image

def obter_numero_pixels(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    largura, altura = imagem.size
    return largura * altura

# Exemplo de uso 

caminho_imagem1 = "IN1LG.jpg"
caminho_imagem2 = "IN1POCO.jpg"

numero_pixels_imagem1 = obter_numero_pixels(caminho_imagem1)
numero_pixels_imagem2 = obter_numero_pixels(caminho_imagem2)

if numero_pixels_imagem1 > numero_pixels_imagem2:
    print("A imagem 1 tem mais pixels.")
elif numero_pixels_imagem1 < numero_pixels_imagem2:
    print("A imagem 2 tem mais pixels.")
else:
    print("As imagens têm a mesma quantidade de pixels.")

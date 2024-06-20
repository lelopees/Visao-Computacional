from PIL import Image

def obter_cores_rgb(imagem_path):
    imagem = Image.open(imagem_path)
    largura, altura = imagem.size
    cores_rgb = []

    for y in range(altura):
        for x in range(largura):
            r, g, b = imagem.getpixel((x, y))
            if (r, g, b) != (255, 255, 255) and (r, g, b) != (0, 0, 0):
                cores_rgb.append((r, g, b))

    return cores_rgb

# Exemplo de uso
imagem_path = 'veressa.jpg'
print('abriu')
cores = obter_cores_rgb(imagem_path)
print(cores)

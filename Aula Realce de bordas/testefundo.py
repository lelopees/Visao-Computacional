from PIL import Image

# Abrir a imagem
img = Image.open("sua_imagem.jpg")

# Converter para RGB (caso não seja)
img = img.convert("RGB")

pixels = img.load()  # criar a matriz de pixels

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b = img.getpixel((i, j))

        # Exemplo: Alterar para preto se o pixel for branco
        if r > 200 and g > 200 and b > 200:
            pixels[i, j] = (0, 0, 0)

# Salvar a imagem modificada
img.save("nova_imagem.jpg")

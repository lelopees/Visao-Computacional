import cv2

def calcular_contraste(imagem):
    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Calcular a variação média dos tons de cinza
    media, desvio_padrao = cv2.meanStdDev(imagem_cinza)
    
    # O contraste é o desvio padrão elevado ao quadrado
    contraste = desvio_padrao**2
    
    return contraste

# Carregar a imagem
imagem = cv2.imread('IN-2poco.jpg')

# Calcular o contraste da imagem
contraste = calcular_contraste(imagem)

# Exibir o resultado
print("Contraste da imagem:", contraste)/home/meat/Downloads/20230707_112008.jpg

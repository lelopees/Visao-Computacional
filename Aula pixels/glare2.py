import cv2
import numpy as np 

# Caminho para a imagem que você quer abrir

marmoreio_image = cv2.imread('1708025048589.jpg')
mask_lea = cv2.imread('1708352497062.jpg')
cv2.imwrite('mask_lea.png', mask_lea)
 
no_glare =  marmoreio_image.copy() 
haha_glare =  mask_lea.copy() 

brilho_global1 = np.mean(np.log1p(marmoreio_image)) 
print('brilho', brilho_global1)
print('brilho traduzido', round(brilho_global1,2))


num_rows = 2    
num_cols = 1     
    
    # Calcular o tamanho de cada parte
height, width =no_glare.shape[:2]
part_height = height // num_rows
part_width = width // num_cols

output_parts = []
no_glare_parts = []
    
# Dividir a imagem em partes e exibi-las
for r in range(num_rows):
    for c in range(num_cols):
        print(r)
        # Calcular as coordenadas de início e fim da parte atual
        start_row = r * part_height
        end_row = (r + 1) * part_height
        start_col = c * part_width
        end_col = (c + 1) * part_width

        # Obter a parte atual da imagem
        part_img = no_glare[start_row:end_row, start_col:end_col] 
        cv2.imwrite('part_img.png', part_img)

        part_lea = mask_lea[start_row:end_row, start_col:end_col]
        cv2.imwrite('part_lea.png', part_lea)

        # blur
        blr = cv2.medianBlur(part_img, 15)
        cv2.imwrite('blr_img.png', blr)

        #hsv
        hsv = cv2.cvtColor(part_img, cv2.COLOR_RGB2HSV)
        val = hsv[:, :, 2]

        cv2.imwrite('hsv_img.png', hsv)

        # at 
        at = cv2.adaptiveThreshold(np.array(255- val), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 15)
        cv2.imwrite('at_img.png', at)# Now invert the threshold, and run another for edges.

        ia = np.array(255 - at)  # inversion of adaptiveThreshold of the value.
                #ia = cv2.cvtColor(ia, cv2.COLOR_BGR2GRAY)
        index_iv = 40 
        iv = cv2.adaptiveThreshold(ia, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, index_iv) 
        cv2.imwrite('iv_img.png', iv)

        ib = cv2.subtract(iv, ia)
        cv2.imwrite('ib_img.png', ib)
        # Turn this to a 3 channel mask. 
        bz = cv2.merge([ib, ib, ib])
        cv2.imwrite('bz_img.png', bz)
        # Use the blur where the mask is, otherwise use the image.
        dsy = np.where(bz == (0, 0, 0), blr, part_img)
        cv2.imwrite('dsy_img.png', dsy)
        result = dsy.copy()
        cv2.imwrite('result_img.png', result)
        # Count the number of pixels with reflex
        num_pixels_reflex = cv2.countNonZero(ia) 
        print('num_pixels_reflex')
        print(num_pixels_reflex)

        meatyPixelArea = cv2.countNonZero(cv2.cvtColor(part_lea, cv2.COLOR_BGR2GRAY))
        print('meatyPixelArea')
        print(meatyPixelArea)

        if num_pixels_reflex != 0 and meatyPixelArea != 0 :
            #print("Pixels AOL:", meatyPixelArea)
            #mask_lea = cv2.cvtColor(mask_lea, cv2.COLOR_BGR2GRAY)
            glarePercentage = (num_pixels_reflex/meatyPixelArea)*100
            #print("Part {r}-{c}%:", glarePercentage)
            # Exibir a parte atual
        else:
            glarePercentage =0
            #print("Part {r}-{c}%:", glarePercentage)

        print('GLARE')
        print(glarePercentage)

        red_intensity = 168# 78 + (182*0.088) + (97*0.585) + (82*0.047) + (glarePercentage*1.41) 

        print('red_intensity')
        print(red_intensity)
                
                # Converter a imagem para escala de cinza
        gray_img = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)                 
        
        white_intensity = 240 

        print('white_intensity')
        print(white_intensity)

        # Criar uma matriz de zeros do mesmo tamanho da imagem
        output_img = np.zeros_like(result)

        # Substituir os pixels de acordo com a intensidade
        mask_red = gray_img < red_intensity
        mask_white = (gray_img >= red_intensity) & (gray_img < white_intensity)

        output_img[mask_red] = [0, 0, 255]  # substituir por vermelho
        output_img[mask_white] = [255, 255, 255]  # substituir por branco

        cv2.imwrite('output1_img.png', output_img)

        # Substituir todos os outros pixels (aqueles com intensidade acima de white_intensity) por branco
        mask_others = ~mask_red & ~mask_white
        output_img[mask_others] = [255, 255, 255]

        cv2.imwrite('output2_img.png', output_img)
        
        output_parts.append(output_img)
        no_glare_parts.append(result) 

 # Criar uma imagem em branco do tamanho total da imagem original
output_img = np.zeros_like(no_glare)
no_glare =np.zeros_like(no_glare)

cv2.imwrite('no_glare2.png', no_glare)


# Copiar cada parte para a posição correta na imagem final
for r in range(num_rows):
    for c in range(num_cols):
        # Calcular as coordenadas de início e fim da parte atual
        start_row = r * part_height
        end_row = (r + 1) * part_height
        start_col = c * part_width
        end_col = (c + 1) * part_width

        # Obter a parte atual da lista de partes
        part_img_output = output_parts[r * num_cols + c]
        part_img_no_glare = no_glare_parts[r * num_cols + c]

        # Copiar a parte para a posição correta na imagem final
        output_img[start_row:end_row, start_col:end_col] = part_img_output
        no_glare[start_row:end_row, start_col:end_col] = part_img_no_glare
        ##Abordagem para remover borda
img= output_img.copy()

cv2.imwrite('img_img.png', img)

# Remove background using bitwise-and operation and mask

mask_lea = cv2.cvtColor(mask_lea, cv2.COLOR_BGR2GRAY)

outImage = cv2.bitwise_and(img, img, mask=mask_lea)
outImage[mask_lea == 0] = [0, 0, 0]  # Turn background black

cv2.imwrite('outImage.png', outImage)


gray = cv2.cvtColor(outImage, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_img.png', gray)

# Limiarização para segmentar os pixels brancos (marmoreio)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # Encontra os contornos dos pixels brancos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Cria uma máscara em branco para o preenchimento
mask = np.zeros_like(outImage)

for contour in contours:
    # Verifica se o contorno tem pelo menos um pixel branco em contato com um pixel preto
    for point in contour:
        x, y = point[0]
        if (
            (x > 0 and gray[y, x - 1] == 0) or  # Pixel à esquerda
            (x < outImage.shape[1] - 1 and gray[y, x + 1] == 0) or  # Pixel à direita
            (y > 0 and gray[y - 1, x] == 0) or  # Pixel acima
            (y < outImage.shape[0] - 1 and gray[y + 1, x] == 0)  # Pixel abaixo
        ):
            area = len(contour)
            if area < 770:
                cv2.drawContours(outImage, [contour], -1, (0, 0, 255), thickness=cv2.FILLED)  # Preenche com vermelho
cv2.imwrite('outImageFinal.png', outImage)
print('finalizado')

# Aplicar o limiar na imagem para obter uma imagem binária
bin_img = cv2.cvtColor(outImage, cv2.COLOR_BGR2GRAY)
        # Contar o número de pixels brancos na imagem binária
white_pixels = np.sum(bin_img == 255)
        
print('aqui_white_pixels')
print(white_pixels)
        # Calculando Marmoreio 
meatyPixelArea = cv2.countNonZero(mask_lea)
print('aqui_meatyPixelArea')
print(meatyPixelArea)
marblePercentage= (white_pixels/meatyPixelArea)*100 


print('marblePercentage')
print(marblePercentage)

def get_marble(marblePercentage):
            if marblePercentage > 18.27:
                return 1100
            data = {
                0.4: 100, 0.45: 110, 0.5: 120, 0.55: 130, 0.6: 140, 0.65: 150, 0.7: 160, 0.75: 170, 0.8: 180, 0.85: 190,
                0.9: 200, 1.03: 210, 1.16: 220, 1.29: 230, 1.42: 240, 1.55: 250, 1.68: 260, 1.81: 270, 1.94: 280, 2.07: 290,
                2.2: 300, 2.312: 310, 2.424: 320, 2.536: 330, 2.648: 340, 2.76: 350, 2.872: 360, 2.984: 370, 3.096: 380,
                3.208: 390, 3.32: 400, 3.427: 410, 3.534: 420, 3.641: 430, 3.748: 440, 3.855: 450, 3.962: 460, 4.069: 470,
                4.176: 480, 4.283: 490, 4.39: 500, 4.627: 510, 4.864: 520, 5.101: 530, 5.338: 540, 5.575: 550, 5.812: 560,
                6.049: 570, 6.286: 580, 6.523: 590, 6.76: 600, 6.895: 610, 7.03: 620, 7.165: 630, 7.3: 640, 7.435: 650,
                7.57: 660, 7.705: 670, 7.84: 680, 7.975: 690, 8.11: 700, 8.377: 710, 8.644: 720, 8.911: 730, 9.178: 740,
                9.445: 750, 9.712: 760, 9.979: 770, 10.246: 780, 10.513: 790, 10.78: 800, 11.053: 810, 11.326: 820,
                11.599: 830, 11.872: 840, 12.145: 850, 12.418: 860, 12.691: 870, 12.964: 880, 13.237: 890, 13.51: 900,
                13.88: 910, 14.25: 920, 14.62: 930, 14.99: 940, 15.36: 950, 15.73: 960, 16.1: 970, 16.47: 980, 16.84: 990,
                17.21: 1000, 17.316: 1010, 17.422: 1020, 17.528: 1030, 17.634: 1040, 17.74: 1050, 17.846: 1060,
                17.952: 1070, 18.058: 1080, 18.164: 1090, 18.27: 1100
            }

            for interval, marble in data.items():
                if marblePercentage <= interval:
                    return marble
            return None

            # Exemplo de uso:
marble = get_marble(marblePercentage)
print('Marmoreio:', marble)   

mask_lea =cv2.cvtColor(outImage, cv2.COLOR_RGB2GRAY)
hh, ww = mask_lea.shape[:2]

cv2.imwrite('mask_lea2.png', mask_lea)


contours = cv2.findContours(mask_lea, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
big_contour = max(contours, key=cv2.contourArea)

rotrect = cv2.minAreaRect(big_contour)
(center), (width,height), angle = rotrect
box = cv2.boxPoints(rotrect)
boxpts = np.intp(box)
#organizando angulo, dependendo da posição da figura, esquerda ou direita
#print('Angle: ', angle)
if angle < -45 and width > height:
    angle = -(90 + angle)
# otherwise, check width vs height
else:
    if angle > -45 and width > height:
        angle = -(-90 +angle)
    else:
        angle= -angle

neg_angle = -angle

M = cv2.getRotationMatrix2D(center, neg_angle, scale=1.0)

rectified = cv2.warpAffine(mask_lea, M, (ww, hh), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
cv2.imwrite('rectified.png', rectified)

###### Desse modo quando tiver dois desenhos seleciono o maior
##cntr = max(contours, key=cv2.contourArea)
x,y,w,h = cv2.boundingRect(big_contour)
# crop to blob limits
crop_marble = rectified[y:y+h, x:x+w]

cv2.imwrite('crop_marble1.png', crop_marble)

#crop= cv2.cvtColor(mask_egs, mask_egs_ori,cv2.COLOR_GRAY2RGB)
crop_marble = cv2.cvtColor(crop_marble,cv2.COLOR_GRAY2RGB)

cv2.imwrite('crop_marble2.png', crop_marble)
##### Substituindo pixels ### Abordagem direta
# Make all perfectly black pixels red
r1, g1, b1 = 29, 29, 29 # Original value
r2, g2, b2 = 255, 0, 0 # Value that we want to replace it with

red, green, blue = crop_marble[:,:,0], crop_marble[:,:,1], crop_marble[:,:,2]
print('blue')
print(blue)
mask_1 = (red == r1) & (green == g1) & (blue == b1)
print(mask_1)
crop_marble[:,:,:3][mask_1] = [0,0,255]    

cv2.imwrite('crop_marbleFinal.png', crop_marble)




       


        
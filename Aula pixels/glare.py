import cv2
import numpy as np

marmoreio_image = cv2.imread('marmoreio_img.jpg')
#0.456                   
no_glare =  marmoreio_image.copy() 

marmoreio_image


brilho_global1 = np.mean(np.log1p(marmoreio_image)) 
print('brilho', brilho_global1)
print('brilho traduzido', round(brilho_global1,2))

num_rows = 2    
num_cols = 1     
    
    # Calcular o tamanho de cada parte
height, width =no_glare.shape[:2]
part_height = height // num_rows
part_width = width // num_cols
    
    # Criar uma lista para armazenar todas as partes da imagem
output_parts = []
no_glare_parts = []

index_at = 15

# Dividir a imagem em partes e exibi-las
for r in range(num_rows):
    for c in range(num_cols):
        # Calcular as coordenadas de início e fim da parte atual
        start_row = r * part_height
        end_row = (r + 1) * part_height
        start_col = c * part_width
        end_col = (c + 1) * part_width
        print('num_rows')
        print(r)          
         
        # Obter a parte atual da imagem
        part_img = no_glare[start_row:end_row, start_col:end_col]
        #part_lea = mask_lea[start_row:end_row, start_col:end_col]
        
        brilho_global0 = np.mean(np.log1p(outImage)) 

        if r == 0:
            outImage = part_img            
            brilho_global0 = np.mean(np.log1p(outImage))  
            print('brilho 0 ', brilho_global0)       
        if r == 1:
            outImage1 = part_img  
            brilho_global1 = np.mean(np.log1p(outImage1)) 
            print('brilho 1', brilho_global1)

        blr = cv2.medianBlur(part_img, 15)
        #print(blr)

        # now grab brightness V of HSV here - but Gray is possibly as good
        hsv = cv2.cvtColor(part_img, cv2.COLOR_RGB2HSV)


        if r == 0:
            outH = hsv                
        if r == 1:
            outH1 = hsv

        val = hsv[:, :, 2]

            #############
            # use ADAPTIVE_THRESH_GAUSSIAN to find spots. 
            # I manually tweaked the values- these seem to work well with what I have.
            #at = cv2.adaptiveThreshold(np.array(255 - scaled_val), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 17)
            ## index_at = 12 pocophone
             ## index_at = 15 LG
                
        if r == 0:
            brilho_global = round(brilho_global0,2)             
        if r == 1:
            brilho_global = round(brilho_global1,2)
        
        print(brilho_global)

        if brilho_global < 0.4:
            index_at = 15
        else:
            index_at = 17
            
        print('index_at', index_at)
        
        at = cv2.adaptiveThreshold(np.array(255- val), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, index_at)

        if r == 0:
            outAt = at                
        if r == 1:
            outAt1 = at

        # Now invert the threshold, and run another for edges.
        ia = np.array(255 - at)  # inversion of adaptiveThreshold of the value.
        #ia = cv2.cvtColor(ia, cv2.COLOR_BGR2GRAY)
        index_iv = 40 
        iv = cv2.adaptiveThreshold(ia, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, index_iv) # 40 nivel de glare ma
        if r == 0:
            outIv = iv                
        if r == 1:
            outIv1 = iv
        # ib = merged edges with the dots (as an invert mask).
        ib = cv2.subtract(iv, ia)

        if r == 0:
            outIb = ib                
        if r == 1:
            outIb1 = ib
        
        # Turn this to a 3 channel mask. 
        bz = cv2.merge([ib, ib, ib])
        # Use the blur where the mask is, otherwise use the image.
        dsy = np.where(bz == (0, 0, 0), blr, part_img)
        result = dsy.copy()
        # Count the number of pixels with reflex
        num_pixels_reflex = cv2.countNonZero(ia)
        #print('Pixels:', num_pixels_reflex)
        #meatyPixelArea = cv2.countNonZero(part_lea)

        #if num_pixels_reflex != 0 and meatyPixelArea != 0 :
            #print("Pixels AOL:", meatyPixelArea)
            #mask_lea = cv2.cvtColor(mask_lea, cv2.COLOR_BGR2GRAY)
            #glarePercentage = (num_pixels_reflex/meatyPixelArea)*100
            #print("Part {r}-{c}%:", glarePercentage)
            # Exibir a parte atual
        #else:
            #glarePercentage =0
            #print("Part {r}-{c}%:", glarePercentage)
        
            ############################################
            ### Meat Color
            #cor_carne_RI=dominant_colors(no_glare)
            #print ('Cor Carne:',cor_carne)
            #### Criando sample com a cor identificacada BGR
            #cv2.imshow('Cor_carne', blank_image)
            #cv2.waitKey(0)
            ### Tranformando BGR em RGB
            #input_RGB_meat_RI=[(cor_carne_RI[1][2],cor_carne_RI[1][1],cor_carne_RI[1][0])]
            #red_intensity = 78 + (input_RGB_meat_RI[0][0]*0.04) + (input_RGB_meat_RI[0][1]*0.585) + (input_RGB_meat_RI[0][2]*0.047) + (glarePercentage*3)
        #red_intensity = 78 + (input_RGB_meat[0][0]*0.088) + (input_RGB_meat[0][1]*0.585) + (input_RGB_meat[0][2]*0.047) + (glarePercentage*1.41)
            #red_intensity = 78 + (input_RGB_meat[0][0]*0.088) + (input_RGB_meat[0][1]*0.585) + (input_RGB_meat[0][2]*0.047) + (glarePercentage*1.41)
            ##############################################################

            # Converter a imagem para escala de cinza
        gray_img = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

            # Definir os valores de intensidade para vermelho e branco (0-255)
            #red_intensity = 110#intensidade para vermelho
        white_intensity = 240 # intensidade para branco

            # Criar uma matriz de zeros do mesmo tamanho da imagem
        output_img = np.zeros_like(result)

            # Substituir os pixels de acordo com a intensidade
        #output_img[np.where(gray_img < white_intensity)] = [255, 255, 255]  # substituir por branco
        #output_img[np.where(gray_img < red_intensity)] = [0, 0, 255]  # substituir por vermelho
        
        output_parts.append(output_img)
        no_glare_parts.append(result)       


cv2.imshow('outImage', outImage)
cv2.imshow('outImage1', outImage1)

cv2.imshow('outH', outH)
cv2.imshow('outH1', outH1)

cv2.imshow('outAt', outAt)
cv2.imshow('outAt1', outAt1)

cv2.imshow('outIv', outIv)
cv2.imshow('outIv1', outIv1)

cv2.imshow('outIb', outIb)
cv2.imshow('outIb1', outIb1)
                   
cv2.waitKey(0)
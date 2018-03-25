

import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import time #importamos la función time para capturar tiempos

file="ivvi_684x684_gray.jpg"
img=cv2.imread(file,0) ## Load an color image in grayscale


if(img.all()==None):
    print("Error al cargar el archivo")
    exit(0)
else:
    print("Elemento cargado : OK")


scale=cv2.CV_16S
#Filtro Gausiano Blue
ImgFilterGauBlue = cv2.GaussianBlur(img,(3,3),0)



#Gradiente en X & Y
                                    # 1,0 significa que la derivida es en el eje x  
sobelx = cv2.Sobel(ImgFilterGauBlue,scale,1,0,ksize=3)
abs_sobelX = np.absolute(sobelx)
sobel_8uX = np.uint8(abs_sobelX)


sobely = cv2.Sobel(ImgFilterGauBlue,scale,0,1,ksize=3)
abs_sobelY = np.absolute(sobely)
sobel_8uY = np.uint8(abs_sobelY)

#Suma aproximada de las dos imagenges, a cada uno se les realizó la derivida en su respectivo componente 
resultado = cv2.addWeighted(sobel_8uX,0.5,sobel_8uY,0.5,0)

#Umbralización de la imagen, lo que hace es convertir el resultado en ceros y unos.
retval,dst= cv2.threshold(resultado,80,255,cv2.THRESH_BINARY)

cv2.imshow('Original',img)
cv2.imshow('Sobel',dst)



cv2.waitKey(0)

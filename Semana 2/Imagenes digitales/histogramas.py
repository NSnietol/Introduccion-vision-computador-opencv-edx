"""
BINS : Es dividir un segmento continuo de numeros en diferentes rangos [(1-10),(10-20),...]
El término BINS en OpenCV se conoce como histSize, en pocas palabras son los intervalos.

DIMS : es la cantidad de parámetros para los que recopilamos los datos. En este caso, recopilamos datos con respecto a una sola cosa, el valor de intensidad. Entonces aquí está 1.

RANGO : Es el rango de valores de intensidad que desea medir. Normalmente, es [0,256], es decir, todos los valores de intensidad.


"""


import cv2
import numpy as np
from time import time #importamos la función time para capturar tiempos
from matplotlib import pyplot as plt




file="ivvi_684x684_gray.jpg"
img=cv2.imread(file,1)


if(img.data==None):
    print("Error")
else:
    print("OK")
    
"""
                    #Histogram Calculation in OpenCV

images : it is the source image of type uint8 or float32.
channels :(En la escala de grises puede tomar los valores RGB=012 ) it is also given in square brackets. It the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0],[1] or [2] to calculate histogram of blue,green or red channel respectively.
mask : mask image. To find histogram of full image, it is given as “None”. But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)
histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
ranges : this is our RANGE. Normally, it is [0,256].

cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
"""

# Esta variable contiene la frecuencia de cada valor de los pixeles en el RGB 0

hist = cv2.calcHist([img],[0],None,[256],[0,256])


print("Open CV")
print(len(hist))

#2. Histogram Calculation in Numpy

print("Numpy")
            #La imagen, hist, rango de pixeles

hist = np.histogram(img.ravel(),256,[0,256])
#Esta es más optima np.bincount(img.ravel(),minlength=256)
 

"""
Plotting Histograms
There are two ways for this,
Short Way : use Matplotlib plotting functions
Long Way : use OpenCV drawing functions

"""

#1. no necesitar calcular el histograma mediante las funciones anteriores, porque matplolib lo hace
#plt.hist(img.ravel(),256,[0,256]); plt.show()


color = ('b','g','r')
for i,col in enumerate(color):
    print(i,col)
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])
plt.show()
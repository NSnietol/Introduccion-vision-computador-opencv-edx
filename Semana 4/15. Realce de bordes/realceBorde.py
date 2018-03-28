"""
El realce de bordes tiene un efecto opuesto a la eliminación de ruido, ya que de
lo que se trata es de resaltar aquellos pixeles que presentan un valor de gris distinto al de
sus vecinos. Por ello, si la imagen es ruidosa, el efecto del ruido se multiplicará; por lo
que antes de resaltar los bordes habrá que eliminar el ruido.
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import time #importamos la función time para capturar tiempos

file="ivvi_684x684_gray.jpg"
img=cv2.imread(file,0) ## Load an color image in grayscale


if(img.data==None):
    print("Error")
else:
    print("OK")


kernel = np.ones((3,3),np.int8)

kernel=kernel*-1

if(kernel.shape[0]==kernel.shape[1]):
    
    kernel[int(kernel.shape[0]/2),int(kernel.shape[1]/2)]=9

dst = cv2.filter2D(img,-1,kernel)
cv2.imshow('Original',img)
cv2.imshow('Laplacina',dst)



cv2.waitKey(0)
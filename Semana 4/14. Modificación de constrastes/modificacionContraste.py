"""
Histograms - 2: Histogram Equalization


"""



import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import time #importamos la función time para capturar tiempos

file="ivvi_low_contrast.jpg"
img=cv2.imread(file,0)


if(img.data==None):
    print("Error")
else:
    print("OK")


#Calcular y mostrar el histograma de la imagen normal, histogram es mas rapido que cv2.calcHist
hist,bins = np.histogram(img.ravel(),256,[0,256])

Original_hist=hist

#Normalizar histOrginal
NormalizeHist=None
NormalizeHist=cv2.normalize(Original_hist,None,0,1,cv2.NORM_MINMAX)

#	// Equalize histogram from a grayscale image	and calcHist
equ = cv2.equalizeHist(img)


hist,bins=np.histogram(equ.ravel(),256,[0,256])
EqualizeHist=hist

#	// Normalizar el histograma ecualizado

EqualizeHistR=None
EqualizeHistR= cv2.normalize(EqualizeHist,None,0,1,cv2.NORM_MINMAX)


plt.plot(NormalizeHist)
plt.show()


plt.plot(EqualizeHist)
plt.show()


res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imshow('res.png',res)

cv2.waitKey(0)
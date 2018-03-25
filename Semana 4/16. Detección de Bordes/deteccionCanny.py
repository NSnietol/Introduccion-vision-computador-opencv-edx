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

edges = cv2.Canny(img,110,160,apertureSize = 3)

cv2.imshow('Original',img)
cv2.imshow('Canny',edges)

cv2.waitKey(0)
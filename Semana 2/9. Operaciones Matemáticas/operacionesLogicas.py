"""
En este script se realizarán operaciones logicas con imagenes.
del contenido de la imagen
Python 3.6.2 |Anaconda custom (64-bit)
add


http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html?highlight=add
Open CV 3.2
"""

import cv2
import numpy as np

file="LSI.jpg"
file2="UC3M.jpg"
img_1=np.zeros((400,400,3)) # Se crea una 'imagen' de color negro completamente
img_2=np.zeros((400,400,3))
res1= cv2.bitwise_not(img_2)
cv2.imshow('Not image 1',res1)

if(img_1.data==None and img_2.data==None):
    print("Error")
else:
    print("OK")
    print(" ",(img_2))
    
#La primera imagen se divide en 2, colocan una sección de color blanco
for i in range(int(img_1.shape[0]/2)):
    for j in range (img_1.shape[1]):
        for RBG in range(3):
            img_1.itemset((j,i,RBG),255)

#En la segunda imagen creamos un rectangulo blanco
img_2[300:370:]=255


"""
itwise Operations
This includes bitwise AND, OR, NOT and XOR operations. They will be highly useful while extracting any part of the image 
"""

cv2.imshow("Imagen 1",img_1)
cv2.imshow("Imagen 2",img_2)

#AND
res= cv2.bitwise_and(img_1,img_2)
cv2.imshow('AND',res)

#OR
res= cv2.bitwise_or(img_1,img_2)
cv2.imshow('OR',res)

#XOR
res= cv2.bitwise_xor(img_1,img_2)
cv2.imshow('XOR',res)

#Not
res= cv2.bitwise_not(img_2)
cv2.imshow('Not image 1',res)


cv2.waitKey(0)


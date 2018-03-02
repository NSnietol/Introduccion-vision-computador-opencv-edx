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
img_1=cv2.imread(file)
img_2=cv2.imread(file2)

if(img_1.data==None and img_2.data==None):
    print("Error")
else:
    print("OK")
    

print("Propiedades\n")
print("Imagne 1",img_1.shape)
print("Imagen 2",img_2.shape)
"""
Necesito crear una imagen blanca y otra negra para cumplir con el ejemplo. 
"""
res=img_1+img_2
#cv2.imshow('Suma de imagenes',res)

res2=cv2.add(img_1,img_2)

##cv2.imshow('Suma de imagenes con Cv2',res2)
"""
AND 
"""

res=cv2.bitwise_and(img_1,img_2)
cv2.imshow('AND',res)


res=cv2.bitwise_or(img_1,img_2)
cv2.imshow('OR',res)


res=cv2.bitwise_not(img_1)
cv2.imshow('Not',res)


res=cv2.bitwise_xor(img_1,img_2)
cv2.imshow('XOR',res2)

cv2.waitKey(0)


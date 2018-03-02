"""
En este script se realizarán operaciones con imagenes.
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
Image Addition
You can add two images by OpenCV function, cv2.add() or simply by numpy operation, 
res = img1 + img2. Both images should be of same depth and type, 
or second image can just be a scalar value.
"""
res=img_1+img_2
#cv2.imshow('Suma de imagenes',res)

res2=cv2.add(img_1,img_2)

##cv2.imshow('Suma de imagenes con Cv2',res2)
"""
There is a difference between OpenCV addition and Numpy addition. 
OpenCV addition is a saturated operation while Numpy addition is a modulo operation.

Image Sustraction 
"""
res=img_1-img_2
#cv2.imshow('Resta de imagenes',res)

res2=cv2.subtract(img_1,img_2)
#cv2.imshow('Resta de imagenes Open CV',res2)

#Image Multiplication

res=img_1*img_2
#cv2.imshow('Resta de imagenes',res)

res2=cv2.multiply(img_1,img_2)
#cv2.imshow('Resta de imagenes Open CV',res2)

#Imagen Divide 

res=img_1/img_2
cv2.imshow('Resta de imagenes',res)

res2=cv2.divide(img_1,img_2)
cv2.imshow('Resta de imagenes Open CV',res2)




cv2.waitKey(0)


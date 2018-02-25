"""
En este script se alteran los  valores de los pixeles buscando borrar la mitad
del contenido de la imagen
Python 3.6.2 |Anaconda custom (64-bit)
Open CV 3.2
"""

import cv2

file="ivvi_684x684_gray.jpg"
img=cv2.imread(file)


if(img.data==None):
    print("Error")
else:
    print("OK")
    print(img)

print("Propiedades\n")
print(img.shape[1])

#Operación optimizada para obtener valores, pixel (683,683)
#Parametros son el pixel y el valor RGB (0,1,2)
print(img.item(68,68,0))

for i in range(int(img.shape[0]/2)):
    for j in range (img.shape[1]):
        for RBG in range(3):
            img.itemset((j,i,RBG),0)

print(img)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

#Muestra
cv2.imshow('image',img)
cv2.waitKey(0)


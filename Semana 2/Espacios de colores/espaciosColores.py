"""

Python 3.6.2 |Anaconda custom (64-bit)
Open CV 3.2
"""

import cv2

file="ivvi_684x684.jpg"
file2="coche-semana2.jpg"
img=cv2.imread(file2)


if(img.data==None):
    print("Error")
else:
    print("OK")
    print(img)

#Splitting and Merging Image Channels
# Se puede usar split o simplemente se accede a la imagen[::], aunque la primera consumo más recuros
#Se sugiere utilizar Numpy, se puede acceder a los dimensiones rgb mediante img[:,:,1=r]
b,g,r = cv2.split(img)
#print(b,g,r)

cv2.imshow('RGB',img)
#Convertimos  la imagen del espacio RGB a HSV
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('HSV',imgHSV)


#Muestra
#cv2.imshow('image',img)
k=cv2.waitKey(0) & 0xFF
if k == 27:
    print("exiting...")
    cv2.destroyAllWindows()


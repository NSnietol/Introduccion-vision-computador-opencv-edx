import cv2
import numpy as np

file='Clase1.jpg'
img = cv2.imread(file)
if(img.size<1):
    print("Error")
else:
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,130,255,0)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    cnt = contours[4]
    imgf = cv2.drawContours(image, [cnt], 0, (0,255,0), 3)

    cv2.imshow('Original',img)
    cv2.imshow('Contorno',imgf)
    cv2.waitKey(0)


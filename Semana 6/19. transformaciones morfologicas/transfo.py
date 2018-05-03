import cv2
import numpy as np

file='LetrasI_BW.jpg'
img = cv2.imread(file,0)
if(img.size<1):
    print("Error")

else:
    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.erode(img,kernel,iterations = 1)

    dilation = cv2.dilate(img,kernel,iterations = 1)

    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


    cv2.imshow('Original',img)
  #  cv2.imshow('Erosion',erosion)
    # cv2.imshow('Dilatacion',dilation)
    # cv2.imshow('Open',opening)
    cv2.imshow('Close',closing)
    cv2.waitKey(0)
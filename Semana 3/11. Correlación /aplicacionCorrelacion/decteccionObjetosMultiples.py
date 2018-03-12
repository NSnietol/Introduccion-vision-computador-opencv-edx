import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
Template Matching with Multiple Objects
In the previous section, we searched image for Messi’s face, which occurs only once in the image. Suppose you are
searching for an object which has multiple occurances, cv2.minMaxLoc() won’t give you all the locations. In that
case, we will use thresholding. So in this example, we will use a screenshot of the famous game Mario and we will
find the coins in it.
"""


img_rgb = cv2.imread('IMG.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('MM.jpg',0)
w, h = template.shape[::-1]


res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
#Crea un arreglo con los puntos que cumple con la condicion que para este caso indican donde estan los elemenots.
loc = np.where( res >= threshold)


for pt in zip(*loc[::-1]):
    #IMAGEN, PUNTOS, color del rectangulo, grosor de la linea
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (45,23,1), 1)
cv2.imshow('res.png',img_rgb)
cv2.waitKey(0)
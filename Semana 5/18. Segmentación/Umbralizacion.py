import cv2
import numpy as np

file='iCab_382x256.jpg'
img_rgb = cv2.imread(file,1)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

img_thres_bin=None
img_thres_bin=cv2.threshold(img_gray,50,250,cv2.THRESH_BINARY)

img_thres_tozero=cv2.threshold(img_gray,50,250,cv2.THRESH_TOZERO)


img_thres_inv=cv2.threshold(img_gray,50,250,cv2.THRESH_BINARY_INV)


cv2.imshow("Original",img_gray)
cv2.imshow("Binario",img_thres_bin[1])
cv2.imshow("Inverse",img_thres_inv[1])
cv2.imshow("To Zero",img_thres_tozero[1])
cv2.waitKey(0)

import cv2
import numpy as np


file="corr_norm.tif"
file2="modelo.tif"
img_norm=cv2.imread(file)
img_modelo=cv2.imread(file2)


if(img_norm.data==None or img_modelo.data==None):
    print("Error")
else:
    print("OK")

print("Propiedades modelo",img_modelo.shape)
print("Propiedades corr_norm",img_norm.shape)

"""

Template Matching is a method for searching and finding the location of a template image in a larger image. 
OpenCV comes with a function cv2.matchTemplate() for this purpose. It simply slides the template image over the input image (as in 2D convolution) and compares the template and patch of input image under the template image.

"""

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
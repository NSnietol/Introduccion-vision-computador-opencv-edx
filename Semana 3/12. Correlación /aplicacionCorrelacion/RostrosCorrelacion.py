
import cv2
import numpy as np
from matplotlib import pyplot as plt


file="IMG.jpg"

template_file="MM.jpg"

img = cv2.imread(file)

template =cv2.imread(template_file)

w, h ,z = template.shape


if(img.data==None or template.data==None):
    print("Error")
else:
    print("OK")

print("Propiedades modelo",template.shape)
print("Propiedades imagen ",img.shape)

"""

Template Matching is a method for searching and finding the location of a template image in a larger image. 
OpenCV comes with a function cv2.matchTemplate() for this purpose. It simply slides the template image over the input image (as in 2D convolution) and compares the template and patch of input image under the template image.

"""


methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

img_norm = img.copy()
    
method =eval(methods[1])

 # OpenCV identificada cada metodo a través de un número(1,2,3,4,5,6)

# Apply template Matching
res = cv2.matchTemplate(img_norm,template,method)

cv2.normalize(res,res,0,1,cv2.NORM_MINMAX)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)



# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum


if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
    
bottom_right = (top_left[0] + (w-30), top_left[1] + (h+30))


cv2.rectangle(img_norm, bottom_right, top_left, (0,0,255),2)



    
bottom_right = (top_left[0] -int(w/2), top_left[1] -int(h/2))
bottom_left = (top_left[0] +int(w/2), top_left[1] +int(h/2))
cv2.rectangle(res, bottom_right,bottom_left, (0,0,255), 2)

cv2.imshow('Resultado Matching',res)
cv2.imshow('Imagen',img_norm)
cv2.waitKey(0)
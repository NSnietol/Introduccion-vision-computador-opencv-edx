
import cv2
import numpy as np
from matplotlib import pyplot as plt


file2="corr_norm.tif"
file="modelo.tif"


img = cv2.imread(file2)
template =cv2.imread(file)

w, h, z = template.shape


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

# Sólo el tercer método falló.


for meth in methods:
    img_norm = img.copy()
    
    method = eval(meth)
    # OpenCV identificada cada metodo a través de un número(1,2,3,4,5,6)


    # Apply template Matching
    res = cv2.matchTemplate(img_norm,template,method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img_norm,top_left, bottom_right,(0,0,255) , 2)

    #Continué con el código de visualización de ejemplo porque es más practico para diferenciar los resultados de la operación que con cv2.imshow
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img_norm,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
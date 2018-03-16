"""

Image blurring is achieved by convolving the image with a low-pass filter kernel. 
It is useful for removing noise. It actually removes high frequency content (e.g: noise, edges)
from the image resulting in edges being blurred when this is filter is applied. 
(Well, there are blurring techniques which do not blur edges).
OpenCV provides mainly four types of blurring techniques.

"""


import cv2
import numpy as np

#Ruido gaussiano
file="ivvi_512x512_gray_rg.jpg"

#Ruido impulsivo
file2="ivvi_512x512_gray_ri.jpg"


file3="ivvi_512x512_gray.jpg"


img_noiseG=cv2.imread(file)

img_noiseI=cv2.imread(file2)


img=cv2.imread(file3)



if(img.data==None  or img_noiseG.data==None):
    print("Error")
    exit(0)
else:

    print("OK")

#cv2.imshow('Ruido Gausiano',img_noiseG)

"""
1. Averaging
This is done by convolving the image with a normalized box filter.
 It simply takes the average of all the pixels under kernel area and replaces the central 
 element with this average. This is done by the function cv2.blur() or cv2.boxFilter().
"""

#El tamaño del kernel es proporcional al suavizado del ruido, no corrige el impulsivo
resBlur=cv2.blur(img_noiseG,(4,4))
#cv2.imshow('Blur vs {0}'.format("as"),resBlur)


"""
2. Gaussian Filtering
In this approach, instead of a box filter consisting of equal filter coefficients,
 a Gaussian kernel is used. It is done with the function, cv2.GaussianBlur(). 
 We should specify the width and height of the kernel which should be positive and odd. 
 We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as equal to sigmaX. If both are given as zeros, they are calculated from the kernel size. Gaussian filtering is highly effective in removing Gaussian noise from the image.

If you want, you can create a Gaussian kernel with the function, cv2.getGaussianKernel().

"""

#Parece que solo me permite colocar el kernel de 5 x 5, no corrige el impulsivo
blur = cv2.GaussianBlur(img_noiseG,(5,5),0)
#cv2.imshow('GaussianBlur vs Gau',blur)


"""
3. Median Filtering
Here, the function cv2.medianBlur() computes the median of all the pixels under the kernel 
window and the central pixel is replaced with this median value. This is highly effective 
in removing salt-and-pepper noise. One interesting thing to note is that, in the Gaussian and 
box filters, the filtered value for the central element can be a value which may not exist in 
the original image. However this is not the case in median filtering, since the central element 
is always replaced by some pixel value in the image. This reduces the noise effectively. 
The kernel size must be a positive odd integer.

"""
#El resultado tiene menos ruido pero la calidad de la imagen se pierde, tambien corrige el impulsivo
median = cv2.medianBlur(img_noiseG,5)
#cv2.imshow('MedianFilter vs Gau',median)



"""
4. Bilateral Filtering
The bilateral filter also uses a Gaussian filter in the space domain, but it also uses one more
(multiplicative) Gaussian filter component which is a function of pixel intensity differences. 
The Gaussian function of space makes sure that only pixels are ‘spatial neighbors’ are considered
for filtering, while the Gaussian component applied in the intensity domain (a Gaussian function 
of intensity differences) ensures that only those pixels with intensities similar to that of the 
central pixel (‘intensity neighbors’) are included to compute the blurred intensity value. As a 
result, this method preserves edges, since for pixels lying near edges, neighboring pixels placed 
on the other side of the edge, and therefore exhibiting large intensity variations when compared 
to the central pixel, will not be included for blurring.
"""

# Es el mejor con el ruido gausiano, pero el impulsuivo no lo corrige
bilitaral = cv2.bilateralFilter(img_noiseG,15,80,80)

"""
15 = Diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from sigmaSpace.


Sigma values: For simplicity, you can set the 2 sigma values to be the same. If they are small (< 10), the filter will not have much effect, whereas if they are large (> 150), they will have a very strong effect, making the image look "cartoonish".

Filter size: Large filters (d > 5) are very slow, so it is recommended to use d=5 for real-time applications, and perhaps d=9 for offline applications that need heavy noise filtering.

This filter does not work inplace.


"""


cv2.imshow('Biltaral',bilitaral)



cv2.waitKey(0)

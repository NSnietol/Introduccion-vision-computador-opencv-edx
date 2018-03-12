import cv2
import numpy as np
img = cv2.imread('IVVI.jpg')

 

"""
                  Scaling
Scaling is just resizing of the image. OpenCV comes with a function cv2.resize() for this purpose. The size of
the image can be specified manually, or you can specify the scaling factor. Different interpolation methods are
used. Preferable interpolation methods are cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) &
cv2.INTER_LINEAR for zooming. By default, interpolation method used is cv2.INTER_LINEAR for all resizing
purposes.

"""


res =cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)
#OR 

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_LINEAR)


cv2.imshow('Scaling 50%',res)
print(res.shape)
cv2.imshow('Original',img)
print(img.shape)


"""
                            Translation
Translation is the shifting of object’s location. If you know the shift in (x,y) direction, let it be (t x , t y ), you can create
the transformation matrix M as follows:

"""
y,x = img.shape[:2]
print(img.shape[:2])
# Recordar la forma de la matriz que permite trasladar la imagen.
#M=[ 0  1 ty ]
#  [ 1  0 tx ]

M = np.float32([[1,0,-15],[0,1,-20]])

res = cv2.warpAffine(img,M,(x,y))
cv2.imshow('Translation',res)

"""
                            Rotation
Rotation of an image for an angle θ is achieved by the transformation matrix of the form
To find this transformation matrix, OpenCV provides a function, cv2.getRotationMatrix2D. Check below example
which rotates the image by 90 degree with respect to center without any scaling

"""
rows,cols = img.shape[:2]
#Mediante esta matriz se realizará la rotación 
M=cv2.getRotationMatrix2D((rows-1,cols-1),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Rotation',dst)




"""
        Reflection

"""
res=cv2.flip(img,1)
cv2.imshow('Reflecton',res)
cv2.waitKey(0)
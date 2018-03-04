
import cv2
import numpy as np

file="IMG.jpg"
img=cv2.imread(file)


if(img.data==None):
    print("Error")
else:
    print("OK")

print("Propiedades\n")
print(img[1])

# Es el filtro a aplicar sobre la imagen, mediante este kernel se realiza un suavisado.
kernel = np.ones((5,5),np.float32)/25

#ddepth (-1) Quiere decir que res va a tener el mismo número bit por pixel que la imagen de entrada
res = cv2.filter2D(img,-1,kernel)
print("Propiedades modificas con el filtro")
print(res[1])

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.namedWindow('res', cv2.WINDOW_NORMAL)
#Muestra
cv2.imshow('image',img)
cv2.imshow('res',res)

cv2.waitKey(0)

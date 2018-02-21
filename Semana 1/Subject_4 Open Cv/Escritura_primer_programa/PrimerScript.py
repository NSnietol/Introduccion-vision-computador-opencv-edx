import cv2

file="ivvi.jpg"
image=cv2.imread(file)


if(image.data==None):
    print("Error")
else:
    print("OK")

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

#Muestra
cv2.imshow('image',image)

#Copia 
cv2.imwrite('messigray.png',image)

cv2.waitKey(0)




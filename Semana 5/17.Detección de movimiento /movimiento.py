

import cv2
import numpy as np

file='IcabMovimientoEscenaEstatica.mp4'
cap = cv2.VideoCapture(file)


fgbg = cv2.createBackgroundSubtractorMOG2(500,100,False)

fore=None
ret, frame = cap.read()
while(frame.all()!=None):
 

    fgbg.setNMixtures(80)

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',frame)
    
    kernel = np.ones((5,5),np.uint8)


    """
    La idea es eliminar ruido
    Morphological transformations are some simple operations based on the image shape. It is normally performed on
    binary images.

    (ERODE)The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always
    try to keep foreground in white).
    """
    cv2.erode(fgmask,kernel,iterations = 1)

    """
    It is just opposite of erosion. Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’. So it increases
    the white region in the image or size of foreground object increases
    """
    cv2.dilate(fgmask,kernel,iterations = 1)

    fgmask=cv2.cvtColor(fgmask,cv2.COLOR_GRAY2BGR)

    res=cv2.bitwise_and(frame,fgmask)
    
    cv2.imshow('destino',res)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    ret, frame = cap.read()
cap.release()
cv2.destroyAllWindows()
"""
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html?highlight=hough

"""

import cv2
import numpy as np

file='su.png'
img = cv2.imread(file)
if(img.size<1):
    print("Error")

else:



 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  
    
 
    edges = cv2.Canny(gray,50,200,apertureSize = 3)

       
 

    lines = cv2.HoughLines(edges,1,np.pi/180,200)
    
    print(lines)

    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(gray,(x1,y1),(x2,y2),(0,0,255),2)

    cv2.imshow('houghlines3.jpg',gray)

    cv2.waitKey(0)
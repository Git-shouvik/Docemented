import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
#Rectangle.
rectangle=cv.rectangle(blank,(110,100),(250,250),(0,0,255),5)
#cv.imshow('Rectangle',rectangle)

#circle
Circle=cv.circle(blank,(60,55),50,(0,255,0),3)
#cv.imshow('Circle',Circle)

#Line
Line=cv.line(blank,(0,0),(300,300),(255,0,0),6)
cv.imshow('Line',Line)

#Text
Text=cv.putText(blank,'OpenCV_Python',(0,350),cv.FONT_HERSHEY_SIMPLEX,2,(255,255,255),1,cv.LINE_AA)
cv.imshow('Text',Text)

cv.waitKey(0)
cv.destroyAllWindows()

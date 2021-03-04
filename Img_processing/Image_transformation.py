import cv2 as cv
import numpy as np

#Resizeing
img=cv.imread('Rover.jpg')
resize=cv.resize(img,(400,400),interpolation=cv.INTER_LINEAR) 
cv.imshow('Resized',resize)
# resize1=cv.resize(img,(300,300),interpolation=cv.INTER_LINEAR)
# cv.imshow('image',resize1)

##Image translation
Tmatrix=np.float32([[1,0,40],[0,1,10]])
dimension=(resize.shape[1],resize.shape[0])
Imagetrans=cv.warpAffine(resize,Tmatrix,dimension)
cv.imshow('Translated img',Imagetrans)

##Image rotation
Rmatrix=cv.getRotationMatrix2D((resize.shape[1]/2,resize.shape[0]/2),90,1)
rotated=cv.warpAffine(resize,Rmatrix,dimension)
cv.imshow('trans',Imagetrans)
cv.imshow('Rotated',rotated)
cv.waitKey(0)
cv.destroyAllWindows()


#edge detection

import cv2 as cv
import numpy as np

img=cv.imread('lena.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Laplacian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

blank=np.zeros(lap.shape[:2],dtype='uint8')
circle=cv.circle(blank,(lap.shape[1]//2,img.shape[0]//2),90,255,-1)
mask=cv.bitwise_and(lap,lap,mask=circle)
cv.imshow('Masked',mask)


#sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined=cv.bitwise_or(sobelx,sobely)

canny=cv.Canny(gray,150,175)
cv.imshow('Canny',canny)

cv.imshow('X',sobelx)
cv.imshow('Y',sobely)
cv.imshow('Combined',combined)
cv.waitKey(0)
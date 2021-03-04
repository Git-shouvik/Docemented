# the mask and the size of the image needs of the same size.
import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg')
print(img.shape)
cv.imshow('lena', img)

blank =np.zeros((320,320), dtype='uint8') #size of the mask should be equal to img.
cv.imshow('Blank Image',blank)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),90,255,-1)
cv.imshow('Mask',mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked_img',masked)
cv.waitKey(10000)
#cv.destroyAllWindows()

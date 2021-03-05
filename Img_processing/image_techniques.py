import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread('Rover.jpg')
img1=cv.imread('alpa.jpg')

resize=cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)  

gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
gray1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur=cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny=cv.Canny(gray,125,75)
cv.imshow('Canny',canny)

#Thresholding
thresh, threshd=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Binary',threshd)

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,0.05)
cv.imshow('Adaptive Thresh',adaptive_thresh)

# Masking 
print('Masking')
blank =np.zeros(threshd.shape[:2], dtype='uint8') #size of the mask should be equal to img.
cv.imshow('Blank Image',blank)

cir=cv.circle(blank,(threshd.shape[1]//2,threshd.shape[0]//5),80,255,-1)
cv.imshow('Mask',cir)
mask=cv.bitwise_and(threshd,threshd,mask=cir)
cv.imshow('Masked_img',mask)

# Histogram
hist=cv.calcHist([gray],[0],mask,[256],[0,254])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')    # Intervals of pixels along x axis
plt.ylabel('No. of pixels')
plt.plot(hist)
plt.xlim([0,256])     # Limit of x axis
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread('lena.jpg')
#cv.imshow('Lena',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Lena',gray)
hist=cv.calcHist([img],[0],None,[256],[0,254])
plt.figure()
# fig=plt.figure()
# ax1=fig.add_subplot(1,2,2)
# ax1.imshow(img)
# ax2=fig.add_subplot(2,2,2)
# ax2.imshow()
plt.title('Histogram')
plt.xlabel('Bins')    
plt.ylabel('No. of pixels')
plt.plot(hist)
plt.xlim([0,256])    
plt.show()

#mat=cv.hconcat([img,gray])
# cv.imshow('mat',mat)
cv.waitKey(0)
cv.destroyAllWindows()

# Histogram computation of three channels

img=cv.imread('lena.jpg')
#cv.imshow('Lena',img)
color=('b','g','r')
for i,col in enumerate(color):
    histCa=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histCa,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
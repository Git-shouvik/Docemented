import cv2 as cv
import numpy as np
img=cv.imread('alpa.jpg')
cv.imshow("bits",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jfif")

cv.imshow('original', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
print(img.shape[:2])

gray = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.blur(src=img, ksize=(3,3))

canny = cv.Canny(blur, 125,175)
cv.imshow('CannyEdge', canny)

# ret, thresh = cv.threshold(src=gray,thresh=125,maxval=250,type=cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')


cv.drawContours(blank, contours,-1,(0,0,255),2)
cv.imshow('Contour', blank)



cv.waitKey(0)
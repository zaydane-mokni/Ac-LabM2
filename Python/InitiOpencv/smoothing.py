import cv2 as cv
import rescale

img = rescale.rescaleFrame(cv.imread("Photos/cat2.jpg"),1)

cv.imshow('original', img)

# Averaging

average = cv.blur(src=img, ksize=(3,3))
cv.imshow('average', average)


# Gaussian Blur

gaussian = cv.GaussianBlur(src=img,ksize=(3,3), sigmaX=0)
cv.imshow('gaussian', gaussian)

# Median blur

median = cv.medianBlur(src=img,ksize= 3)
cv.imshow('median', median)

# Bilateral blur must effectif

bilat = cv.bilateralFilter(src=img,d=5,sigmaColor=15,sigmaSpace=15)
cv.imshow('bilat', bilat)

cv.waitKey(0)
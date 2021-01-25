import cv2 as cv
import numpy as np


img = cv.imread("Photos/cat2.jpg")
blank = np.zeros((img.shape[0], img.shape[1]), dtype='uint8')

cv.imshow('original', img)
cv.imshow('blank', blank)

mask = cv.circle(img= blank, center=(img.shape[1]//2 +45, img.shape[0]//2+45), radius=100, color= 255, thickness=-1)
#mask = cv.rectangle(img= img, pt1 = img.shape[1]//2, pt2= img.shape[0]//2, color=(0,255,0), thickness=-1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread("Photos/boston.jfif")

cv.imshow('original', img)

#Blank image

blank = np.zeros(img.shape[:2], dtype='uint8')


# Split
b,g,r = cv.split(img)

cv.imshow('bleu',b)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape) # 3 representes 3 colour chanel Blue Green Red
print(b.shape)
print(g.shape)
print(r.shape)

# Merge

merged = cv.merge(mv=[b,g,r])
cv.imshow('merge',merged)


Blue = cv.merge(mv=[b,blank,blank])
cv.imshow('Blue_Only', Blue)

Green = cv.merge(mv=[blank,g,blank])
cv.imshow('Green_Only', Green)

Red = cv.merge(mv=[blank,blank,r])
cv.imshow('Red_Only', Red)


cv.waitKey(0)
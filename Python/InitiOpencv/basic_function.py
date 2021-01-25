import cv2 as cv
import rescale

img = rescale.rescaleFrame(cv.imread('Photos/1.jpg'),0.2)

cv.imshow('origianl', img)


#Converting to grayscale

gray = cv.cvtColor(src=img, code = cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Blur an image

blur = cv.blur(src=img, ksize=(3,3))
cv.imshow('Blur', blur)

Gaussain_blur = cv.GaussianBlur(src=img, ksize=(3,3), sigmaX=2)
cv.imshow('Gaussain_blur', Gaussain_blur)


# Edge  Cascade

canny = cv.Canny(image=blur,threshold1=125, threshold2=175)
cv.imshow('Canny', canny)

canny2 = cv.Canny(image=img,threshold1=125, threshold2=175)
cv.imshow('Canny2', canny2)

#Dilating the image

dilated = cv.dilate(src=canny,kernel=(7,7), iterations=7)
cv.imshow('Dilated', dilated)

#Eroding

eroded = cv.erode(src=dilated,kernel=(3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize

resized = cv.resize(src=img,dsize=(500,500))
cv.imshow('Resized', resized)

# Cropping

croped = img[50:200,200:400]
cv.imshow('Cropped',croped)

cv.waitKey(0)
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/cat.jfif")

cv.imshow('original', img)

#plt show image in RGB
#plt.imshow(img)
#plt.show()


# BGR => Grayscale
gray = cv.cvtColor(src=img, code= cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#  BGR => HSV (hue saturation value)

hsv = cv.cvtColor(src=img, code= cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR => LAB
lab = cv.cvtColor(src=img, code= cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)

# BGR => RGB
rgb = cv.cvtColor(src=img, code= cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

#plt.imshow(rgb)
#plt.show()

cv.waitKey(0)
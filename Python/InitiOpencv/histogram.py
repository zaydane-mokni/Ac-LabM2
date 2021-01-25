import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/cat2.jpg")

cv.imshow('img', img)


#Gray

gray = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Gray histp
"""gray_hist = cv.calcHist(images=[gray], channels=[0],mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.show()"""


# Color Histograme
color = ('b','g','r')
for i,col in enumerate(color):
    hist = cv.calcHist(images=[img], channels=[i],mask=None, histSize=[256], ranges=[0,256])
    plt.plot(hist, color=col)

plt.show()

cv.waitKey(0)
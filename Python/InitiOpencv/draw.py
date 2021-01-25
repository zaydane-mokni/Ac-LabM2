import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#1. Paint the image a certain colour
"""
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)"""

#2. draw rectangle

cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)


#3. Draw circle

cv.circle(img=blank, center = (blank.shape[1]//2, blank.shape[0]//2), radius=40, color= (0,0,255), thickness=3)
cv.imshow('Circle', blank)

#4. Draw line
cv.line(img = blank,pt1=(100,250), pt2= (300,400), color= (255,255,255), thickness=3)
cv.imshow('Line', blank)

#5. Write Text

cv.putText(img=blank, text="Hello",org=(0,400), fontFace= cv.FONT_HERSHEY_TRIPLEX,fontScale=1.0,color= (0,0,255), thickness=2)
cv.imshow('Text', blank)



cv.waitKey(0)

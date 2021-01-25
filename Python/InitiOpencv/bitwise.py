import cv2 as cv
import rescale
import numpy as np


blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(), pt1=(30,30), pt2=(370,370),color=255, thickness=-1)
cv.imshow('rectangle', rectangle)

circle = cv.circle(blank.copy(),center=(blank.shape[1]//2,blank.shape[0]//2),radius=200,color=255, thickness=-1)
cv.imshow('circle', circle)

# Bitwise  AND

bitwise_and = cv.bitwise_and(circle, rectangle)
cv.imshow('bitwise_and', bitwise_and)


cv.waitKey(0)
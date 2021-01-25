import cv2 as cv
import numpy as np

import rescale

img = rescale.rescaleFrame(cv.imread(filename='Photos/1.jpg'),0.1)

cv.imshow("Img", img)

# Translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimension= (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100,100)
cv.imshow('translate', translated)

# Rotation

rotate = cv.rotate(src=img, rotateCode=cv.ROTATE_90_CLOCKWISE)

print(cv.ROTATE_90_CLOCKWISE*0.5)
cv.imshow('rotate', rotate)

# Flip flipCode=-1 ==> return verticaly and 0 ==> flip horizontaly

flip = cv.flip(src=img,flipCode=1)
cv.imshow('flip', flip)





cv.waitKey(0)

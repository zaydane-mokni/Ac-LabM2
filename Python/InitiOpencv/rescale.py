import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Work for videos, images, lives
    width = int(frame.shape[1] * scale)
    heidth = int(frame.shape[0] * scale)
    dimension = (width, heidth)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)
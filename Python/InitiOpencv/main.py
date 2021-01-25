import cv2 as cv
import rescale
# Read img
"""img = cv.imread('Photos/2.jpg')
print(f'width:{img.shape[1]}\nheight:{img.shape[0]}')

img_rescale = rescale.rescaleFrame(img,0.1)
print(f'width:{img_rescale.shape[1]}\nheight:{img_rescale.shape[0]}')

cv.imshow('cat',img)
cv.imshow('cat_rescale',img_rescale)

cv.waitKey(0)"""
#Read video

def changeRes(width, heigth):
    # Only work with live
    capture.set(3,width)
    capture.set(4,heigth)

capture = cv.VideoCapture('Videos/source.gif')

while True:
    isTrue, frame = capture.read() #get the video frame by frame

    frame_resized = rescale.rescaleFrame(frame)

    cv.imshow('Video', frame)  # display the video frame by frame
    cv.imshow('Video_resised', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'): #if press d ==> break the loop
        break

capture.release()
cv.destroyAllWindows()
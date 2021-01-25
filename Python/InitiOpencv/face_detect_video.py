import cv2 as cv
import rescale

img = rescale.rescaleFrame(cv.imread('Photos/people2.jfif'),1.5)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
cap = cv.VideoCapture(1)

while True:

    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(image = gray, scaleFactor=1.1, minNeighbors=5)

    print(f'number of faces found: {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=2)
        cv.putText(img=frame, text='Ariless',org=(x,y+h+50), fontFace= cv.FONT_HERSHEY_TRIPLEX,fontScale=1.0,color= (0,0,255), thickness=2)
    if cv.waitKey(1) & 0xFF == ord('d'): #if press d ==> break the loop
        break

    cv.imshow('detected_face', frame)

cap.release()
cv.destroyAllWindows()
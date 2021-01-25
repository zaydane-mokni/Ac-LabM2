import os
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

labels = os.listdir('Data')
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainner.yml')

img = cv.imread('Data/Maked/maksssksksss415.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)

    if confidence >=95:
        cv.putText(img, 'Masked', (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2)
        cv.rectangle(img, (x,y), (x+w,y+h), (0,0,255), thickness=2)
    else:
        cv.putText(img, 'Not Masked', (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2)
        cv.rectangle(img, (x,y), (x+w,y+h), (0,0,255), thickness=2)
cv.imshow('Detected Face', img)

cv.waitKey(0)
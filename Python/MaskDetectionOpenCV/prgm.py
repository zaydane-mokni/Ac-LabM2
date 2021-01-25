import cv2 as cv
import numpy as np

haar_face = cv.CascadeClassifier('haar_face.xml')
recognizer=cv.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")


cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(src=frame,
                       code=cv.COLOR_BGR2GRAY)

    img_with_blur = cv.blur(src=gray,
                            ksize=(3,3))
    face_rect = haar_face.detectMultiScale(image=img_with_blur,
                                           scaleFactor=1.5,
                                           minNeighbors=4)
    for x,y,w,h in face_rect:
        roi=gray[y:y+h, x:x+w]
        label, confidence =recognizer.predict(roi)
        if confidence<=95 :
            frame = cv.rectangle(img=frame,
                                 pt1=(x,y),
                                 pt2=(x+w,y+h),
                                 color=(0,255,0),
                                 thickness=2)
            cv.putText(frame, f'Masked {np.round(confidence,2)}',
                       (x+10, y-10),
                       cv.FONT_HERSHEY_SIMPLEX,
                       0.9,
                       (0,255,0), 2)
        else:
            frame = cv.rectangle(img=frame,
                                 pt1=(x,y),
                                 pt2=(x+w,y+h),
                                 color=(0,0,255),
                                 thickness=2)
            cv.putText(frame,
                       f'Not Masked {np.round(confidence,2)}',
                       (x+10, y-10),
                       cv.FONT_HERSHEY_SIMPLEX,
                       0.9,
                       (0,0,255),
                       2)

    cv.imshow('Mask detection', frame)

    cv.waitKey(1)
import cv2 as cv
import pickle
import numpy as np

face_cascade= cv.CascadeClassifier('haarcascade_frontalface_alt2.xml')
recognizer=cv.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
id_image=0
color_info=(255, 255, 255)
color_ko=(0, 0, 255)
color_ok=(0, 255, 0)

with open("labels.pickle", "rb") as f:
    og_labels=pickle.load(f)
    labels={v:k for k, v in og_labels.items()}

cap=cv.VideoCapture('movie.avi')
while True:
    ret, frame=cap.read()
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, scaleFactor=1.2,minNeighbors=4, minSize=(50, 50))
    for (x, y, w, h) in faces:
        roi_gray=gray[y:y+h, x:x+w]
        id_, conf=recognizer.predict(roi_gray)
        if conf<=95:
             color=color_ok
             name=labels[id_]
        else:
            color=color_ko
            name="Inconnu"

        cv.putText(frame, f'{name} {np.round(conf,2)}', (x, y-10), cv.FONT_HERSHEY_DUPLEX, 1, color_info, 1, cv.LINE_AA)
        cv.rectangle(frame, (x, y), (x+w, y+h), color, 2)
    cv.imshow('FaceDetection', frame)
    key=cv.waitKey(1)&0xFF
    if key==ord('q'):
        break
    if key==ord('a'):
        for cpt in range(100):
            ret, frame=cap.read()

cv.destroyAllWindows()
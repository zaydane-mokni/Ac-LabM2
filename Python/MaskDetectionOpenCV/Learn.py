import cv2 as cv
import os
import numpy as np

Dir = r"C:\Users\arile\Desktop\Cours Master\M2\HackLab\MakDetection\Data"
types = os.listdir('Data')

haar_face= cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

for root, dirs, files in os.walk(Dir):
    for type in types:
        path = os.path.join(Dir, type)
        lab = types.index(type)
    for img in os.listdir(path):
        img_path = os.path.join(path, img)

        img_array = cv.imread(img_path)
        gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

        faces_rect = haar_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        for (x, y, w, h) in faces_rect:
            faces_roi = gray[y:y + h, x:x + w]
            features.append(faces_roi)
            labels.append(lab)

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('trainner.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
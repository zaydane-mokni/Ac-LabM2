import os
import cv2 as cv
import numpy as np

people = os.listdir('Faces')
DIR = r'C:\Users\arile\Desktop\Cours Master\M2\HackLab\OpencvTutoFreeCodeCamp\Faces'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

paths= []

for j in range(len(people)-3):
    paths.append(os.path.join(DIR,people[j]))
    for root,dir, files in os.walk(paths[j]):
        for i in range(len(files)):
            img = cv.imread(os.path.join(root,files[i]))
            gray = cv.cvtColor(src=img, code= cv.COLOR_BGR2GRAY)
            faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=2, minSize=(50, 50))
            for (x,y,w,h) in faces:
                cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv.putText(img=img,text=people[j],org=(int(img.shape[1]*0.10),int(img.shape[0])),fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=2, color=255, thickness=2)
            cv.imshow(f'{people[j]},{i+1}',img)
cv.waitKey(0)
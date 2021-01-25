import cv2 as cv


cap = cv.VideoCapture(1)
haar_face = cv.CascadeClassifier('haar_face.xml')

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(src=frame,code=cv.COLOR_BGR2GRAY)
    img_with_blur = cv.blur(src=gray,ksize=(3,3))
    face_rect = haar_face.detectMultiScale(image=img_with_blur, scaleFactor=1.1, minNeighbors=5,)
    #face rec nous donne des coordonées [x,y,w,h]
    #print(f'Nombre de Visage detecté : {len(face_rect)}')
    print(ret)
    for x,y,w,h in face_rect:
        frame = cv.rectangle(img=frame, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=2)
        cv.putText(frame, 'Ariless', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

    cv.imshow('Ari', frame)

    cv.waitKey(1)


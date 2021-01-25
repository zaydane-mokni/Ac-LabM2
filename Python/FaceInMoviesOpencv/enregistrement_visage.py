import cv2 as cv

""" fichier permetant d'identifier des visages """
face_cascade = cv.CascadeClassifier('./haarcascade_frontalface_alt2.xml')


""" Mon film """
cap = cv.VideoCapture('movie.avi')

id=0
while True:
    ret, frame=cap.read()
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(50,50))
    for x, y, w, h in face:
        cv.imwrite("non_classees/p-{:d}.png".format(id), frame[y:y+h, x:x+w])
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        id += 1
    key = cv.waitKey(1)&0xFF
    if key==ord('q'):
        break
    if key==ord('a'):
        for cpt in range(100):
            ret, frame=cap.read()

    cv.imshow('video', frame)

cap.release()
cv.destroyAllWindows()
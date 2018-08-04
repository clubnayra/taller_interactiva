import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# importamos el modelo entrenado
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detectamos rostros
    faces = face_cascade.detectMultiScale(gray, 1.3,2)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),4)
        smiles = smile_cascade.detectMultiScale(gray[x:x+w, y:y+h], 1.3, 2)
        for (xs, ys, ws,hs) in smiles:
            cv2.rectangle(frame,(x+xs,y+ys),(x+xs+ws,y+ys+hs),(0,255,255),3)
            

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
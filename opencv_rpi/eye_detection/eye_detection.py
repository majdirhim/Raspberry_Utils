import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalcatface.xml')

eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        if len(eyes) :
            cv2.putText(img, "eyes open", (x,y-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        else :
            cv2.putText(img, "eyes closed", (x,y-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
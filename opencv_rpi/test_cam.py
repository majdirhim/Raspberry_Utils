import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)

        if cv2.waitKey(30) & 0xff == ord('q'): # press 'Q' to quit
            break
    else :
        print("No camera !! Check index")
cap.release()
cv2.destroyAllWindows()
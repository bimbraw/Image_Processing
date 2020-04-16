import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture(0)

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #print(frame.size)

    # Our operations on the frame come here
    #frame = imutils.resize(frame, width=800)
    #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#640
    #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#480
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.putText(gray, '.', (320, 240), cv2.FONT_HERSHEY_COMPLEX,
                       1, (255,0,0), 2, cv2.LINE_4)
    #gray = cv2.line(gray, (0, 0), (511, 511), (255, 0, 0), 5)
    gray = cv2.rectangle(gray, (200, 350), (260, 420), (255, 0, 0), 3)
    gray = cv2.rectangle(gray, (260, 350), (320, 420), (255, 0, 0), 3)
    gray = cv2.rectangle(gray, (320, 350), (380, 420), (255, 0, 0), 3)
    gray = cv2.rectangle(gray, (380, 350), (440, 420), (255, 0, 0), 3)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

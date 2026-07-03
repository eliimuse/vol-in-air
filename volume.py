import cv2 as cv
import mediapipe as mp
import numpy as np
import time
import hand_module as hm
import math
from pycaw.pycaw import AudioUtilities

wCam, hCam = 640,480
cap = cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
ptime = 0
detector = hm.handDetector(detectionConf=0.7)

# Volume Control
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
print(f"Audio output: {device.FriendlyName}")
smoothVol = volume.GetMasterVolumeLevelScalar()
prevVol = smoothVol

# Smoothing factor 
alpha = 0.2
volbar = 400
volper = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList)!=0:
        #print(lmList[4],lmList[8])

        x1,y1 = lmList[4][1], lmList[4][2]      # thumb tip
        x2,y2 = lmList[8][1], lmList[8][2]      # index tip
        cx,cy = (x1+x2)//2, (y1+y2)//2

        cv.circle(img,(x1,y1),9,(255,0,0),cv.FILLED)
        cv.circle(img,(x2,y2),9,(255,0,0),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(0,150,255),thickness=2)
        cv.circle(img,(cx,cy),9,(255,0,0),cv.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        targetVol = np.interp(length, [40, 220], [0.0, 1.0])
        smoothVol = alpha * targetVol + (1 - alpha) * smoothVol

        # Update only if change is noticeable
        if abs(smoothVol - prevVol) > 0.01:
            volume.SetMasterVolumeLevelScalar(smoothVol, None)
            prevVol = smoothVol

        currentVol = volume.GetMasterVolumeLevelScalar()
        volbar = np.interp(currentVol, [0, 1], [400, 150])
        volper = int(currentVol * 100.2)

        if length < 45:
            cv.circle(img, (cx, cy), 12, (0, 255, 0), cv.FILLED)


    cv.rectangle(img,(50,150),(85,400),(250,150,0),3)
    cv.rectangle(img,(50,int(volbar)),(85,400),(250,150,0),cv.FILLED)
    cv.putText(img, f'{int(volper)}%', (35,440), cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),thickness=2)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(img, f'FPS: {int(fps)}', (10,50), cv.FONT_HERSHEY_COMPLEX,1,(255,150,255),thickness=2)

    cv.imshow('Volume control',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
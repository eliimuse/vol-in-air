import cv2 as cv
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionConf=0.5, trackConf=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConf = detectionConf 
        self.trackConf = trackConf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,min_detection_confidence=self.detectionConf,min_tracking_confidence=self.trackConf)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img, draw = True):
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.res = self.hands.process(imgRGB)
    
        if self.res.multi_hand_landmarks:
            for handLms in self.res.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self,img,handNo=0, draw=True):
        lmList = []
        if self.res.multi_hand_landmarks:
            myHand = self.res.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    centx, centy = int(lm.x*w), int(lm.y*h)
                    lmList.append([id, centx, centy])
                    if draw:
                        cv.circle(img,(centx,centy),8,(255,0,0),cv.FILLED)
        return lmList

def main():
    ptime = 0
    ctime = 0
    cap = cv.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList)!=0:
            print(lmList[4])

        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN,2,(255,0,255),thickness=2)

        cv.imshow('Image',img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()

import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)    cTime = time.time()

                if (id==8):
                    cv2.circle(img, (cx,cy), 25, (255, 0 ,0), cv2.FILLED)

cTime = 0
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #Fps meter

    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,0),3)


    cv2.imshow("Video", img)
    cv2.waitKey(1)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)



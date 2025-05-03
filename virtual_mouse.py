import cv2
import numpy as np
import mediapipe as mp
import autopy
import time
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
screen_width, screen_height = autopy.screen.size()
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * wCam), int(lm.y * hCam)
                lmList.append((id, cx, cy))

            if lmList:
                x1, y1 = lmList[8][1:]  # Index Finger Tip
                x2, y2 = lmList[12][1:]  # Middle Finger Tip

                # Move mouse
                screen_x = np.interp(x1, (100, wCam - 100), (0, screen_width))
                screen_y = np.interp(y1, (100, hCam - 100), (0, screen_height))
                autopy.mouse.move(screen_x, screen_y)

                # Click gesture
                distance = np.hypot(x2 - x1, y2 - y1)
                if distance < 30:
                    autopy.mouse.click()

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

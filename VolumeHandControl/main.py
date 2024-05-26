import cv2
import mediapipe as mp
import time

from handtracking import HandDetector


mphands = mp.solutions.hands
hands = mphands.Hands()

mpDraw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)


if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

detector = HandDetector(detectionCon=0.95)
cTime = 0
pTime = 0

while True:
    ret, frame = cap.read()

    frame = detector.findHands(frame, draw=True)
    lmsList = detector.findPosition(frame, draw=False)
    print(lmsList)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
    )
    if not ret:
        print("Error: Cannot receive frame.")
        break

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

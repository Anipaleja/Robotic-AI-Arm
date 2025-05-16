from cvzone.HandTrackingModule import HandDetector
import cv2
from adafruit_servokit import ServoKit
import time

pin_index = 0
pin_thumb = 2
pin_ring = 4
pin_pinky = 10
pin_middle = 14

kit = ServoKit(channels=16)

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # index
        if fingers[1] == 0:
            #pass
            print("1", end = ", ")
            kit.servo[pin_index].angle = 90

        elif fingers[1] == 1:
            #pass
            print("0", end = ", ")
            kit.servo[pin_index].angle = 0

        # thumb
        if fingers[0] == 0:
            #pass
            print("1", end = ", ")
            kit.servo[pin_thumb].angle = 180

        elif fingers[0] == 1:
            #pass
            print("0", end = ", ")
            kit.servo[pin_thumb].angle = 0

        # ring
        if fingers[3] == 0:
            #pass
            print("1", end = ", ")
            kit.servo[pin_ring].angle = 0

        elif fingers[3] == 1:
            #pass
            print("0", end = ", ")
            kit.servo[pin_ring].angle = 100

        # pinky
        if fingers[4] == 0:
            #pass
            print("1", end = ", ")
            kit.servo[pin_pinky].angle = 0

        elif fingers[4] == 1:
            #pass
            print("0", end = ", ")
            kit.servo[pin_pinky].angle = 100

        # middle
        if fingers[2] == 0:
            #pass
            print("1")
            kit.servo[pin_middle].angle = 0

        elif fingers[2] == 1:
            #pass
            print("0")
            kit.servo[pin_middle].angle = 180

    cv2.imshow("img", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    elif cv2.waitKey(1) & 0xFF == "0":
        #kit.servo[0].angle = 0
        #kit.servo[1].angle = 0
        #kit.servo[2].angle = 0
        #kit.servo[3].angle = 0
        #kit.servo[4].angle = 0
        time.sleep(1)
        #pass

    time.sleep(0.05)

cv2.cap.release()
cv2.destroyAllWindows()

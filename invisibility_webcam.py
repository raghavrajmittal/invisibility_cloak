'''Wear your invisibility cloak in front of your webcam'''
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

background = None
while True:
    if background is None:
        time.sleep(3)
        ret, frame = cap.read()
        background = frame
        continue

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,100,20])
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170,100,20])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask0 + mask1
    output = frame.copy()
    output[np.where(mask!=0)] = background[np.where(mask!=0)]
    # output[np.where(mask==0)] = 0

    cv2.imshow('output', output)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()

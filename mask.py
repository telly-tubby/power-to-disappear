import cv2
import numpy as np

cap = cv2.VideoCapture(0);
for i in range(60):
    _, bg = cap.read()
    bg = np.flip(bg, axis=1)
while cap.isOpened():
    ret, img = cap.read()
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ub = np.array([137, 255, 255])
    lb = np.array([77, 128, 40])
    mask = cv2.inRange(hsv, lb, ub)
    mask1 = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(img, img, mask=mask1)
    res1 = cv2.bitwise_and(bg, bg, mask=mask)
    final = cv2.add(res, res1)
    cv2.imshow('image', img)
    #cv2.imshow('mask', mask)
    #cv2.imshow('mask1', mask1)
    cv2.imshow('final', final)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
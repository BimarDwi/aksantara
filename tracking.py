import cv2
import numpy as np

cap = cv2.VideoCapture("Red Dot.mp4")

lower_limit = np.array([0, 50, 50])
upper_limit = np.array([10, 255, 255])

while True:
    ret, frame = cap.read()

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(frame_hsv, lower_limit, upper_limit)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        cnt = max(contours, key = cv2.contourArea)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Red Circle", frame)
    key = cv2.waitKey(1)
    if key == 113:
        break

cap.release()
cv2.destroyAllWindows()

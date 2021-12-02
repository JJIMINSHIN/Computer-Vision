import cv2
import numpy as np


cap = cv2.VideoCapture('./images/walking.avi')
#영상의 프레임수
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

fgbg = cv2.createBackgroundSubtractorMOG2()
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', fgmask)
    cv2.imshow('bg', fgbg.getBackgroundImage())
    #차이 보기
    # cv2.imshow('frame', frame)
    # cv2.imshow('bg', fgmask)
    if cv2.waitKey(1) & 0xff == 27:   #27은 esc
        break


cap.release()
cv2.destroyAllWindows()
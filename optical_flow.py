from os import terminal_size
import cv2
import numpy as np
from numpy.core.fromnumeric import reshape


cap = cv2.VideoCapture('./images/walking.avi')
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

#optical frame 방향과 거리 계산

color = np.random.randint(0, 255, (200, 3))
lines = None
prev_img = None

terminate = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)

#영상출력하기 위해 while문 사용

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    img_draw = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if prev_img is None:    #첫번째는 이전프레임이 없으므로
        prev_img = gray
        lines = np.zeros_like(frame)
        prev_pt = cv2.goodFeaturesToTrack(prev_img, 200, 0.01, 10)
    else: 
        next_img = gray
        next_pt, status, err = cv2.calcOpticalFlowPyrLK(prev_img, next_img, prev_pt, None, criteria=terminate)
        prev_mv = prev_pt[status == 1]
        next_mv = next_pt[status == 1]
        for i, (p, n) in enumerate(zip(prev_mv, next_mv)):  #라인을 그리기 위해
            px, py = p.ravel()
            nx, ny = n.ravel()
            cv2.line(lines, (px, py), (nx, ny), color[i].tolist(), 2)
            cv2.circle(img_draw, (nx, ny), 2, color[i].tolist(), -1)  #채워넣어서 -1
        
        img_draw = cv2.add(img_draw, lines)
        prev_img = next_img
        prev_pt = next_mv, reshape[-1, 1, 2]  #차원으로 변경
    
    cv2.imshow('Optical-flow', img_draw)
    if cv2.waitKey(delay) == 27:
        break
    elif cv2.waitKey(delay) == 8:
        prev_img = None 

cap.release()
cv2.destroyAllWindows()
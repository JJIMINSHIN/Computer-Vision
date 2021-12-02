import cv2
import numpy as np

cap = cv2.VideoCapture('./images/cctv.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
thresh = 100
max_diff = 20
a = None 
b = None
c = None

if cap.isOpened():
    ret, a = cap.read() #프레임 하나씩 받아오기
    ret, b = cap.read()
    while True:
        ret, c = cap.read()
        #보여줄것

        frame = c.copy()

        grey_a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        grey_b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        grey_c = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

        diff1 =cv2.absdiff(grey_a, grey_b)   #diff 절대값 
        diff2 =cv2.absdiff(grey_b, grey_c)


        ret, diff1_thresh = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)
        ret, diff2_thresh = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)


        diff = cv2.bitwise_and(diff1_thresh, diff2_thresh)  # 1,2 차이될때 리턴됨
        diff_cnt = cv2.countNonZero(diff)

        if diff_cnt > max_diff:
            non_zero = np.nonzero(diff) # 픽셀값이 0이 아니면 해당 좌표값 리턴
            x1 = min(non_zero[1])
            y1 = min(non_zero[0])
            x2 = max(non_zero[1])
            y2 = max(non_zero[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        

        stacked = np.hstack((frame, cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)))
        cv2.imshow('cctv', stacked)

        a = b        
        b = c 

        if cv2.waitKey(24) == ord('q'):
            break
            
else:
    print("Can't open it")

cap.release()
cv2.destroyAllWindows()
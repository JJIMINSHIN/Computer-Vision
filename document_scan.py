import cv2
import numpy as np


win_name = 'scanner'
img = cv2.imread('./images/paper.jpg')

pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)
draw = img.copy()

def on_mouse(event, x, y, flags, param):
    global pts_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0 , 255, 0), -1)
        cv2.imshow(win_name, draw)

        pts[pts_cnt] = [x,y]
        pts_cnt += 1

        if pts_cnt == 4:
            sm = pts.sum(axis=1)
            diff = np.diff(pts, axis=1)

            top_left = pts[np.argmin(sm)]
            bottom_right = pts[np.argmax(sm)]

            top_right = pts[np.argmin(sm)]
            bottom_left = pts[np.argmax(sm)]

            pts1 = np.array([
                top_left, top_right, bottom_left, bottom_right
            ], dtype=np.float32)
            
            w1 = abs(bottom_right[0]-bottom_left[0])
            w2 = abs(top_right[0]-top_left[0])

            h1 = abs(top_right[1]-bottom_left[1])
            h2 = abs(top_left[1]-bottom_left[1])

            width = max([w1, w2])
            height = max([h1, h2])

            pts2 =np.array([
                [0, 0], [width-1, 0], [width-1, height-1], [0, height-1]
            ], dtype=np.float32)

            # print(pts1)
            # print(pts2)

            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(img, matrix, (int(width), int(height)))
            cv2.imshow('scanned',result)

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, on_mouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

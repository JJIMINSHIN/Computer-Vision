import cv2
import numpy as np


#코너 탐지하는 프로그래밍 
#edge탐색 -> 경계 찾기 

img = cv2.imread('./images/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corner = cv2.cornerHarris(gray, 2, 3, 0.04)  #3코너 탐색하고 엣지찾을거라서 
#코너 좌표
coord = np.where(corner > 0.1 * corner.max())
coord = np.stack((coord[1], coord[0]), axis=-1)

#동그라미 그리기(x,y 재구성)

for x, y in coord:
    cv2.circle(img, (x, y), 5, (0, 0, 255), 1, cv2.LINE_AA)

#normalize 
corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)
merge = np.hstack((corner_norm, img))



cv2.imshow('Harris', merge)
cv2.waitKey()
cv2.destroyAllWindows()

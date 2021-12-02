import cv2
import numpy as np


img = cv2.imread('./images/cat-01.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#키포인트 추출1
# gitt = cv2.GFTTDetector_create()
# keypoints = gitt.detect(gray, None)
# img_draw = cv2.drawKeypoints(img, keypoints, None)

#키포인트 추출2
# detector = cv2.SimpleBlobDetector_create()
# keypoints = detector.detect(gray, None)
# img_draw = cv2.drawKeypoints(img, keypoints, None)

#키포인트 추출3
detector = cv2.SIFT_create()  #책에는 버전업 전으로 되어있어서 동일
keypoints = detector.detect(gray, None)
img_draw = cv2.drawKeypoints(img, keypoints, None)

###현재로서는 잘 안쓰임 , 엑스박스 

cv2.imshow('GITT', img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()
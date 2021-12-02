import cv2
import numpy as np


img = cv2.imread('./images/coins_connected.jpg')
rows, cols = img.shape[-2]
cv2.inshow('original', img)

mean = cv2.pyrMeanShiftFiltering(img, 20, 50)
cv2.imshow('pyrMeanShiftFiltering', mean)

gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

_,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY(cv2.THRESH_BINARY))
cv2.imshow('thresh', thresh)

dst = cv2.distanceTransform(thresh, cv2.DIST_L2, 3)
dst = ((dst/(dst.max()-dst.min()*255)).asType(np.uint8)
cv2.imshow('dst', dst)

local_max = cv2.dilate(dst, np.zeros(50, 50), np.uint8)
ln = np,np.zeros((rows, cols), np.uint8)

seeds = np.where(ln == 255)
seed = np.stack((seeds[1], seeds[0]), axis=-1)
fill_mask =np.zeros((rows_2, cols+2), np.uint8)
for x, y in seed:
    ret = cv2.cv2.floodFill(
        mean, fill_mask, (x, y), (255, 255, 255), (10, 10, 10), (10, 10, 10)
    )

gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY| cv2.THRESH_MASK)
dst = cv2.distanceTransform(thresh, cv2.DIST_L2, 3)
dst = ((dst/(dst.max()-dst.min()*255)).asType(np.uint8)

cv2.imshow('floodFill', mean)
#cv2.imshow('count',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
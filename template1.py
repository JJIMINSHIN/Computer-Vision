import cv2
import numpy as np


img = cv2.imread('./images/figures.jpg')
template = cv2.imread('./images/taekwonv1.jpg')
th, tw = template.shape[:2]
cv2.imshow('template', template)


img_draw = img.copy()
res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED) #제곱차이매칭 TM_SQDIFF_NORMED

#최소값과 최대값을 가지고 가운데 박스 만들기 (min, max 좌표값)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(min_val, max_val, min_loc, max_loc)

#가운데 박스 그리기
top_left = min_loc
match_val = min_val

bottom_right = (top_left[0] + tw, top_left[1] + th)
cv2.rectangle(img_draw, top_left, bottom_right, (0 ,255, 0), 2) #박스의 두께 2
cv2.imshow('result',img_draw)



cv2.waitKey(0)
cv2.destroyAllWindows()


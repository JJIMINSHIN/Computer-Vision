import cv2
import numpy as np


img = cv2.imread('./images/figures.jpg')
template = cv2.imread('./images/taekwonv1.jpg')

#90도로 회전시켜서
#template = cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE)
#np.rot90로 도리는것도 있음
th, tw = template.shape[:2]
cv2.imshow('template', template)

methods =['cv2.TM_SQDIFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_CCOEFF_NORMED']

for i, method_name in enumerate(methods):

    img_draw = img.copy()
    method = eval(method_name)
    res = cv2.matchTemplate(img, template, method)  #제곱차이매칭 TM_SQDIFF_NORMED


    #최소값과 최대값을 가지고 가운데 박스 만들기 (min, max 좌표값)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)

    #TM_SQDIFF 1에 가까울수록 좋은 결과치, 
    if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:

        #가운데 박스 그리기
        top_left = min_loc
        match_val = min_val

    else:
        top_left = max_loc
        match_val = max_val

    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(img_draw, top_left, bottom_right, (0, 255, 0), 2)  #박스의 두께 2
    cv2.putText(
        img_draw, str(match_val), top_left,
        cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2, cv2.LINE_AA
    )
    cv2.imshow(method_name, img_draw)  #결과치마다 윈도우 네임 달라짐



cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import numpy as np

image1 = cv2.imread('./images/cat-01.jpg')
image2 = image1.astype(np.uint16)
b, g, r = cv2.split(image2)
gray1 = ((b+g+r)/3).astype(np.unit8)

gray2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

dummy_grey1 = np.zeros_like(image1, dtype=np.uint8)
dummy_grey2 = np.zeros_like(image1, dtype=np.uint8) 
dummy_grey2 = np.zeros_like((443, 444, 3))
print(image1.shape, gray1.shape, gray2.shape)
#(443, 444, 3)(443, 444, 3)(443, 444, 3)

#cv2.imshow('raw',image1)
#cv2.imshow('gray1',gray1)
#cv2.imshow('gray2',gray2)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
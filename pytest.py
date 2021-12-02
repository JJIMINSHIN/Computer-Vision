import cv2
import numpy as np
import matplotlib.pyplot as plt

def conv2d(image, kernel):
    kernel = np.flipud(np.fliplr(kernel))
    output = np.zeros_like(image)
    
#이미지 줄어드는걸 방지
    padded_image =np.zeros((image.shape[0]+2, image.shape[1]+2))
    padded_image[1:-1, 1:-1] = image #첫번쨰부터 마지막 첫번째까지 이미지 집어넣기
    
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            output[y,x] = (kernel*padded_image[y:y+3, x:x+3]).sum()
    
    return output

src = cv2.imread('./images/cat-01.jpg')
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

kernel = np.array([
    [1,2,1],
    [2,4,2],
    [1,2,1]
])*(1/16)

dst =conv2d(src,kernel)
plt.imshow(dst, cmap='gray')
plt.show()
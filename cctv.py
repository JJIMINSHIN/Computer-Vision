import cv2

cap = cv2.VideoCapture('./images/cctv.mp4')


if cap.isOpened():
    while True:
        ret, frame = cap.read()
        cv2.imshow('cctv',frame)

        if cv2.waitKey(24) == ord('q'):
            break
            
else:
    print("Can't open it")

cap.release()
cv2.destroyAllWindows()
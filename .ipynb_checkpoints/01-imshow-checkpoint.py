import cv2

cap = cv2.VideoCapture('./images/AuroraBorealis.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)
print(f'FPS: {fps}, Delay: {delay}')

if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (1280,720))
            cv2.imshow('aurora', frame)
            cv2.waitKey(delay)
        else:
            break
else:
    print("can't open video file")

cap.release()
cv2.destroyAllWindows()
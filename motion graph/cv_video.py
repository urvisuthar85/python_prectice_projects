import cv2, time

video = cv2.VideoCapture(0)

#time.sleep(2)
a = 0
while True:
    
    a += 1 
    check,fream = video.read()

    print(check)
    print(fream)
    gray = cv2.cvtColor(fream,cv2.COLOR_RGB2GRAY)
    cv2.imshow('capture',gray)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()

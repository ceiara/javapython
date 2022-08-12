import cv2
import numpy as np

img = cv2.imread('20220811/gora.jpg', cv2.IMREAD_COLOR)

cv2.imshow('gora',img)
cv2.waitKey(0)

print(img.shape)
try:
    for i in range(100):
        x = np.random.randint(0,181,1)[0]
        endx = x+100
        y = np.random.randint(0,121,1)[0]
        endy = y+100

        print(x, ' ', endx)
        print(y, ' ', endy)

        roi = img[30:endx,40:endy]
        print(roi.shape)
        
        x = np.random.randint(0,181,1)[0]
        endx = x+100
        y = np.random.randint(0,121,1)[0]
        endy = y+100

        print(x, ' ', endx)
        print(y, ' ', endy)

        img[0:120,0:120] = roi

        cv2.imshow('gora',img)
        cv2.waitKey(0)
except Exception as e:
    print(e)
import cv2
import numpy as np

img = np.zeros((450,700,3), dtype= 'uint8')
cv2.namedWindow('IMAGE')

def blue(x):
    img[:,:,0] = x

def green(x):
    img[:,:,1] = x

def red(x):
    img[:,:,2] = x

cv2.createTrackbar('Blue','IMAGE',0,255,blue)
cv2.createTrackbar('Green','IMAGE',0,255,green)
cv2.createTrackbar('Red','IMAGE',0,255,red)

while True:
    cv2.imshow('IMAGE',img)
    k = cv2.waitKey(10)

    if k == ord('q'):
        break
cv2.destroyAllWindows()
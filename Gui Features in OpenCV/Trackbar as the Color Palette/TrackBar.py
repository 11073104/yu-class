"""
@author: wuxin
"""
import cv2 as cv
import numpy as np

def nothing(x):
    pass

if __name__ == "__main__":
    # 创建一副黑色图像
    img = cv.imread('messi5.jpg')
    cv.namedWindow('image')

    cv.createTrackbar('R', 'image', 0, 255, nothing)
    cv.createTrackbar('G', 'image', 0, 255, nothing)
    cv.createTrackbar('B', 'image', 0, 255, nothing)

    switch = '0:OFF\n1:ON'
    cv.createTrackbar(switch, 'image', 0, 1, nothing)

    while(1):
        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')
        s = cv.getTrackbarPos(switch, 'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv.destroyAllWindows()
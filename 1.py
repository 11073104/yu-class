#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:40:12 2021

@author: ros
"""

import cv2 as cv
import numpy as np


def nothing(x):
    pass
if __name__ == "__main__":
       
        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')
        
        
cv.namedWindow('image')

cv.createTrackbar('r', 'image', 0, 255, nothing)
cv.createTrackbar('g', 'image', 0, 255, nothing)
cv.createTrackbar('b', 'image', 0, 255, nothing)

# 设置默认值
img_path = "messi5.jpg"
img = cv.imread(img_path)

while (True):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
     break

     r = cv.getTrackbarPos('R', 'image')
     g = cv.getTrackbarPos('G', 'image')
     b = cv.getTrackbarPos('B', 'image')
     


    
cv.destroyAllWindows()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:19:54 2021

@author: ros
"""

import cv2
import numpy as np
def nothing(x):
pass
# 创建一副墀色图像
img = cv.imread('messi5.jpg', 0)

cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
switch='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
while(1):
cv2.imshow('image',img)
k=cv2.waitKey(1)&0xFF
if k==27:
break
r=cv2.getTrackbarPos('R','image')
g=cv2.getTrackbarPos('G','image')
b=cv2.getTrackbarPos('B','image')
s=cv2.getTrackbarPos(switch,'image')
if s==0:
img[:]=0
else:
img[:]=[b,g,r]
cv2.destroyAllWindows()
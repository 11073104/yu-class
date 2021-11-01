#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:31:42 2021

@author: ros
"""

import cv2
import numpy as np
def nothing(x):
 pass
# 创建一副墀色图像
 img=np.zeros((300,512,3),np.uint8)
 cv2.namedWindow('image')
 cv2.createTrackbar('R','image',0,255,nothing)
 cv2.createTrackbar('G','image',0,255,nothing)
 cv2.createTrackbar('B','image',0,255,nothing)



 cv2.imshow('image',img)
 k=cv2.waitKey(0)&0xFF
 if k==27:

 r=cv2.getTrackbarPos('R','image')
 g=cv2.getTrackbarPos('G','image')
 b=cv2.getTrackbarPos('B','image')


 cv2.destroyAllWindows()
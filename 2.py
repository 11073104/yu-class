#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:58:01 2021

@author: ros
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def Change_threhole(x):
 # get current positions of four trackbars
  T1 = cv2.getTrackbarPos('T1','home_canny')
  T2 = cv2.getTrackbarPos('T2','home_canny')
  edges = cv2.Canny(img,T1,T2)
  cv2.imshow('home_canny',edges)
  cv2.imshow('home',img)
  
cv2.namedWindow('home_canny', cv2.WINDOW_NORMAL) #WINDOW_AUTOSIZE 
cv2.namedWindow('home', cv2.WINDOW_NORMAL) #WINDOW_AUTOSIZE   
  
cv2.createTrackbar('T1','home_canny',0,500,Change_threhole)
cv2.createTrackbar('T2','home_canny',0,500,Change_threhole)

img = cv2.imread('messi5.jpg',0)
edges = cv2.Canny(img,150,300)   ##initial value
cv2.imshow('home_canny',edges)
cv2.imshow('home',img)

k = cv2.waitKey(0) & 0xFF
if k == 27:
 cv2.destroyAllWindows()


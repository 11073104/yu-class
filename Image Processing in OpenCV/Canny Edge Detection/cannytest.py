# -*- coding: utf-8 -*-
"""
@author: wuxin
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

if __name__ == "__main__":
    img = cv.imread("messi5.jpg", 0)
    cv.createTrackbar('low_threshold', 'image', 0, 100, nothing)
    cv.createTrackbar('high_threshold', 'image', 101, 255, nothing)
    edges = cv.Canny(img,' low_threshold', 'high_threshold')
    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original Image')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray'), plt.title('Edge Image')
    plt.xticks([]), plt.yticks([])

    plt.show()

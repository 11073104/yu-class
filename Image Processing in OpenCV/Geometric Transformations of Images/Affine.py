# -*- coding: utf-8 -*-
"""
@author: wuxin
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":

    img = cv2.imread('drawing.jpg')

    rows, cols, ch = img.shape

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv2.getAffineTransform(pts1, pts2)

    dst = cv2.warpAffine(img, M, (cols, rows))
    dst = dst.astype(np.uint8)

    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.xticks([]), plt.yticks([])
    plt.show()

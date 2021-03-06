import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

if __name__ == "__main__":

    img = cv.imread('home.png')
    b, g, r = cv.split(img)
    img = cv.merge([r, g, b])
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

    plt.subplot(121), plt.imshow(img), plt.title('img')
    plt.subplot(122), plt.imshow(hist, interpolation='nearest'), plt.title('hist')
    plt.show()
# -*- coding: utf-8 -*-
import cv2 
  
# import Numpy 
import numpy as np 
from matplotlib import pyplot as plt

# Image read
img = cv2.imread('./Images/lotus.jpg', 0) # gray-scale image
img = cv2.resize(img, (500, 500))
size = img.shape[0]
# Cut off Frequency
Do = 50
# High pass Filter using Distance Matrix
def FilterDesign(img, size, Do):
    # D is distance Matrix
    D = np.zeros([size, size], dtype=np.uint32)
    # H is Filter
    H = np.zeros([size, size], dtype=np.uint8)
    r = img.shape[0] // 2
    c = img.shape[1] // 2
    # Distance Vector
    for u in range(0, size):
        for v in range(0, size):
            D[u, v] = abs(u - r) + abs(v - c)
    # Using Cut off frequncy applying 0 and 255 in H to make a High Pass Filter and center = 1
    for i in range(size):
        for j in range(size):
            if D[i, j] > Do:
                H[i, j] = 255
            else:
                H[i, j] = 0
    return H
# High Pass Filter
H = FilterDesign(img, size, Do)

# Applying fft and shift
input = np.fft.fftshift(np.fft.fft2(img))
# Multiplying image with High Pass Filter
out = input*H
# Taking Inverse Fourier of image
out = np.abs(np.fft.ifft2(np.fft.ifftshift(out)))
out = np.uint8(cv2.normalize(out, None, 0, 255, cv2.NORM_MINMAX, -1))
# Gradient image after applying High pass filter

plt.subplot(2, 3, 1), plt.imshow(img, 'gray'),plt.title('Original Image')
plt.subplot(2, 3, 2), plt.imshow(H, 'gray'),plt.title('High Pass Filter')
plt.subplot(2, 3, 3), plt.imshow(out, 'gray'),plt.title('High Pass Filtered Image')
plt.subplot(2, 3, 4), plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 3, 6), plt.hist(out.ravel(),256,[0,256]),plt.title('Histogram of High Pass Filtered Image')
plt.show()
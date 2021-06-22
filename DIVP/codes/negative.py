import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('Images/hist1.bmp',0)

neg=cv2.bitwise_not(img1)

plt.subplot(2,2,1),plt.imshow(img1, 'gray'),plt.title('Original Image')
plt.subplot(2,2,2),plt.imshow(neg, 'gray'),plt.title('Negated Image')
plt.subplot(2,2,3),plt.hist(img1.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2,2,4),plt.hist(neg.ravel(),256,[0,256]),plt.title('Histogram of Negated Image')
plt.show()
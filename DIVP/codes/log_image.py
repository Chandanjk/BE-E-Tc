import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('Images/babyincradle.png',0)

c = 255 / np.log(1 + np.max(img1)) 
log_image = c * (np.log(img1 + 1)) 
log_image = np.array(log_image, dtype = np.uint8)

plt.subplot(2, 2, 1), plt.imshow(img1, 'gray'),plt.title('Original Image')
plt.subplot(2, 2, 2), plt.imshow(log_image, 'gray'),plt.title('Image after Log Transformation')
plt.subplot(2, 2, 3), plt.hist(img1.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 2, 4), plt.hist(log_image.ravel(),256,[0,256]),plt.title('Histogram of Image after Log Transformation')
plt.show() # To show figure
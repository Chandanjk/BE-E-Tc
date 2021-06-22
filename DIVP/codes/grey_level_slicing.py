import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load the image
img = cv2.imread('images/goldfish.tif',0)
# Find width and height of image
row, column = img.shape
# Create an zeros array to store the sliced image
img1 = np.zeros((row,column),dtype = 'uint8')
img2 = np.zeros((row,column),dtype = 'uint8')
 
# Specify the min and max range
min_range = 10
max_range = 150
 
# Loop over the input image and if pixel value lies in desired range set it to 255 otherwise set it to 0.
for i in range(row):
    for j in range(column):
        #without background
        if img[i,j]>min_range and img[i,j]<max_range:
            img1[i,j] = 180    #without background
            img2[i,j] = img[i,j] + 30    #with background
        else:
            img1[i,j] = 0    #without background
            img2[i,j] = img[i,j]    #with background
        
# Display the image
plt.subplot(2, 3, 1), plt.imshow(img, 'gray'),plt.title('Original Image')
plt.subplot(2, 3, 2), plt.imshow(img1, 'gray'),plt.title('Gray Level Sliced Image without Background')
plt.subplot(2, 3, 3), plt.imshow(img2, 'gray'),plt.title('Gray Level Sliced Image with Background')
plt.subplot(2, 3, 4),plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 3, 5),plt.hist(img1.ravel(),256,[0,256]),plt.title('Histogram of Image sliced without Background')
plt.subplot(2, 3, 6),plt.hist(img2.ravel(),256,[0,256]),plt.title('Histogram of Image sliced with Background')
plt.show()

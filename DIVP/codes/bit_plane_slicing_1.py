import numpy as np
import cv2
from matplotlib import pyplot as plt
# Read the image in greyscale
img = cv2.imread('images/zoneplate.png',0)
 
row, column = img.shape
# Create an zeros array to store the sliced image
img0 = np.zeros((row,column),dtype = 'uint8')
img1 = np.zeros((row,column),dtype = 'uint8')
img2 = np.zeros((row,column),dtype = 'uint8')
img3 = np.zeros((row,column),dtype = 'uint8')
img4 = np.zeros((row,column),dtype = 'uint8')
img5 = np.zeros((row,column),dtype = 'uint8')
img6 = np.zeros((row,column),dtype = 'uint8')
img7 = np.zeros((row,column),dtype = 'uint8')
 
# Loop over the input image and if pixel value lies in desired range set it to 255 otherwise set it to 0.
for i in range(row):
    for j in range(column):
        img0[i,j] = img[i,j] & 1
        img1[i,j] = img[i,j] & 2
        img2[i,j] = img[i,j] & 4
        img3[i,j] = img[i,j] & 8
        img4[i,j] = img[i,j] & 16
        img5[i,j] = img[i,j] & 32
        img6[i,j] = img[i,j] & 64
        img7[i,j] = img[i,j] & 128
# Display the image
plt.subplot(3, 3, 1), plt.imshow(img, 'gray'),plt.title('Original Image')
plt.subplot(3, 3, 2), plt.imshow(img0, 'gray'),plt.title('Plane 0')
plt.subplot(3, 3, 3), plt.imshow(img1, 'gray'),plt.title('Plane 1')
plt.subplot(3, 3, 4), plt.imshow(img2, 'gray'),plt.title('Plane 2')
plt.subplot(3, 3, 5), plt.imshow(img3, 'gray'),plt.title('Plane 3')
plt.subplot(3, 3, 6), plt.imshow(img4, 'gray'),plt.title('Plane 4')
plt.subplot(3, 3, 7), plt.imshow(img5, 'gray'),plt.title('Plane 5')
plt.subplot(3, 3, 8), plt.imshow(img6, 'gray'),plt.title('Plane 6')
plt.subplot(3, 3, 9), plt.imshow(img7, 'gray'),plt.title('Plane 7')
plt.show()

cv2_subt = cv2.subtract(img, img7 )   #It should be a dark image
plt.imshow(cv2_subt, 'gray'),plt.title('Subtracted plane 7 from original image')
plt.show()
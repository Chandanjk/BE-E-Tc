import cv2 
import numpy as np 
from matplotlib import pyplot as plt

def powerlaw(img,y): 
    height,width=img.shape
    img4 = np.zeros((height,width),dtype = 'uint8')
    for i in range(width):
        for j in range(height):
            img4[j,i] = 255*(img[j,i]/255) ** y
    img4 = np.array(img4, dtype = np.uint8)
    return img4

# read a image using imread 
img = cv2.imread('Images/flower.jpg',0)

img1 = powerlaw(img , 0.4)
img2 = powerlaw(img , 1)
img3 = powerlaw(img , 1.6)

plt.subplot(2, 4, 1),plt.imshow(img, 'gray'),plt.title('Original Image') 
plt.subplot(2, 4, 2),plt.imshow(img1, 'gray'),plt.title('Power Law Transformed Image for y=0.4')
plt.subplot(2, 4, 3),plt.imshow(img2, 'gray'),plt.title('Power Law Transformed Image for y=1')
plt.subplot(2, 4, 4),plt.imshow(img3, 'gray'),plt.title('Power Law Transformed Image for y=1.6')
plt.subplot(2, 4, 5), plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 4, 6), plt.hist(img1.ravel(),256,[0,256]),plt.title('Histogram for Image with y=0.4')
plt.subplot(2, 4, 7), plt.hist(img2.ravel(),256,[0,256]),plt.title('Histogram for Image with y=1')
plt.subplot(2, 4, 8), plt.hist(img3.ravel(),256,[0,256]),plt.title('Histogram for Image with y=1.6')
plt.show()
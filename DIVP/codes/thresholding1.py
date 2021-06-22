from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

def getThreshold(img , threshold):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] < threshold: #set img pixel value=0 if original pixel value is less than 0 otherwise 255
                img[i,j] = 0
            else : img[i,j] = 255
    return img

#Read an image          
img = cv2.imread('img11.tif',0);

#show original image
plt.figure(0)
plt.imshow(img , cmap=plt.cm.gray)
plt.title('Original image ')

#plot histogram of original image
plt.figure(1)
plt.hist(img.ravel() , bins=256)
plt.title('Histogram of original image')

threshold = 150 #set threshold from histogram
thresh_img = getThreshold(img , threshold) #get thresholded image

#show the image after thresholding
plt.figure(2)
plt.imshow(thresh_img , cmap=plt.cm.gray)
plt.title('Image after thresholding')

plt.show()
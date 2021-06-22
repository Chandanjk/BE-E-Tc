import cv2 
  
# import Numpy 
import numpy as np 
from matplotlib import pyplot as plt

def min_filter(img):
    height,width=img.shape
    img_pad = np.zeros((height+2,width+2),dtype = 'uint8')
    img_pad_out = np.zeros((height+2,width+2),dtype = 'uint8')
    img2 = np.zeros((height,width),dtype = 'uint8')
    for i in range(0,width):
        for j in range(0,height):
            img_pad[j+1,i+1]=img[j,i]
    height1,width1=img_pad.shape
    s=258;
    for i in range(0,width1-2):
        for j in range(0,height1-2):
            for l in range(i,i+3):
                for m in range(j,j+3):
                    if(img_pad[m,l]<=s):
                        s=img_pad[m,l]
            img_pad_out[j+1,i+1]=s;
            s=258;
    for i in range(0,width):
        for j in range(0,height):
            img2[j,i]=img_pad_out[j+1,i+1]
    return img2

def max_filter(img):
    height,width=img.shape
    img_pad = np.zeros((height+2,width+2),dtype = 'uint8')
    img_pad_out = np.zeros((height+2,width+2),dtype = 'uint8')
    img2 = np.zeros((height,width),dtype = 'uint8')
    for i in range(0,width):
        for j in range(0,height):
            img_pad[j+1,i+1]=img[j,i]
    height1,width1=img_pad.shape
    s=0;
    for i in range(0,width1-2):
        for j in range(0,height1-2):
            for l in range(i,i+3):
                for m in range(j,j+3):
                    if(img_pad[m,l]>=s):
                        s=img_pad[m,l]
            img_pad_out[j+1,i+1]=s;
            s=0;
    for i in range(0,width):
        for j in range(0,height):
            img2[j,i]=img_pad_out[j+1,i+1]
    return img2

def median_filter(img):
    height,width=img.shape
    img_pad = np.zeros((height+2,width+2),dtype = 'uint8')
    img_pad_out = np.zeros((height+2,width+2),dtype = 'uint8')
    img2 = np.zeros((height,width),dtype = 'uint8')
    for i in range(0,width):
        for j in range(0,height):
            img_pad[j+1,i+1]=img[j,i]
    height1,width1=img_pad.shape
    for i in range(0,width1-2):
        for j in range(0,height1-2):
            num = [ img_pad[j,i],img_pad[j+1,i],img_pad[j+2,i],img_pad[j,i+1],img_pad[j+1,i+1],img_pad[j+2,i+1],img_pad[j,i+2],img_pad[j+1,i+2],img_pad[j+2,i+2] ];
            num.sort();
            img_pad_out[j+1,i+1]=num[4];
    for i in range(0,width):
        for j in range(0,height):
            img2[j,i]=img_pad_out[j+1,i+1]
    return img2

# read a image using imread 
img1 = cv2.imread('Images/min_max_filter/img1.jpeg',0)

img2=min_filter(img1)
img3=max_filter(img1)
img4=median_filter(img1)

plt.subplot(2, 4, 1),plt.imshow(img1, 'gray'),plt.title('Original Image') 
plt.subplot(2, 4, 2),plt.imshow(img2, 'gray'),plt.title('Min Filtered Image')
plt.subplot(2, 4, 3), plt.imshow(img3, 'gray'),plt.title('Max Filtered Image')
plt.subplot(2, 4, 4), plt.imshow(img4, 'gray'),plt.title('Median Filtered Image')
plt.subplot(2, 4, 5), plt.hist(img1.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 4, 6), plt.hist(img2.ravel(),256,[0,256]),plt.title('Histogram of Min Filtered Image')
plt.subplot(2, 4, 7), plt.hist(img3.ravel(),256,[0,256]),plt.title('Histogram of Max Filtered Image')
plt.subplot(2, 4, 8), plt.hist(img4.ravel(),256,[0,256]),plt.title('Histogram of Median Filtered Image')
plt.show()
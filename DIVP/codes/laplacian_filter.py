import cv2 
  
# import Numpy 
import numpy as np 
from matplotlib import pyplot as plt

def convo(img,k):
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
            s=(img_pad[j,i]*k[0,0])+(img_pad[j,i+1]*k[0,1])+(img_pad[j,i+2]*k[0,2])+(img_pad[j+1,i]*k[1,0])+(img_pad[j+1,i+1]*k[1,1])+(img_pad[j+1,i+2]*k[1,2])+(img_pad[j+2,i]*k[2,0])+(img_pad[j+2,i+1]*k[2,1])+(img_pad[j+2,i+2]*k[2,2]);
            img_pad_out[j+1,i+1]=s/9;
    img_pad = np.array(img_pad, dtype = np.uint8)
    for i in range(0,width):
        for j in range(0,height):
            img2[j,i]=img_pad_out[j+1,i+1]
    return img2+img


# read a image using imread 
img1 = cv2.imread('Images/laplacian/coin.jpg',0)
#Laplacian Filtering
k1 = np.array((
	[-1, -1, -1],
	[-1, 8, -1],
	[-1, -1, -1]), dtype="int")
img2=convo(img1,k1)

#High Boost Filtering
k2 = np.array((
	[-1, -1, -1],
	[-1, 9, -1],
	[-1, -1, -1]), dtype="int")
img3=convo(img1,k2)

plt.subplot(2, 3, 1),plt.imshow(img1, 'gray'),plt.title('Original Image') 
plt.subplot(2, 3, 2),plt.imshow(img2, 'gray'),plt.title('Laplacian Filtered Image')
plt.subplot(2, 3, 3),plt.imshow(img3, 'gray'),plt.title('High Boost Filtered Image')
plt.subplot(2, 3, 4), plt.hist(img1.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 3, 5), plt.hist(img2.ravel(),256,[0,256]),plt.title('Histogram of Laplacian Filtered Image')
plt.subplot(2, 3, 6), plt.hist(img3.ravel(),256,[0,256]),plt.title('Histogram of High Boost Filtered Image')
plt.show()
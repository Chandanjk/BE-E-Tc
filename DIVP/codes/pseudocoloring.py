import cv2 
  
# import Numpy 
import numpy as np 
from matplotlib import pyplot as plt

# read a image using imread 
img = cv2.imread('Images/tajmahal1.jpg',0)
h,w=img.shape

colored = np.zeros(shape=(h,w,3))

for i in range(0,w):
    for j in range(0,h):
        if(img[j,i]>=0 and img[j,i]<=31):
            colored[j,i,0] = img[j,i];
        elif(img[j,i]>=32 and img[j,i]<=63):
            colored[j,i,1] = img[j,i];
        elif(img[j,i]>=64 and img[j,i]<=95):
            colored[j,i,2] = img[j,i];
        elif(img[j,i]>=96 and img[j,i]<=127):
            colored[j,i,0] = img[j,i]+10;
           
        elif(img[j,i]>=128 and img[j,i]<=159):
            colored[j,i,0] = img[j,i]-10;
            colored[j,i,1] = img[j,i]-20;
            colored[j,i,2] = img[j,i]+15;
        elif(img[j,i]>=160 and img[j,i]<=191):
            colored[j,i,0] = img[j,i]-10;
            colored[j,i,1] = img[j,i]-10;
            colored[j,i,2] = img[j,i]+15;
        elif(img[j,i]>=192 and img[j,i]<=223):
            colored[j,i,2] = img[j,i]+15;
        else:
            colored[j,i,0] = img[j,i]-10;
            colored[j,i,1] = img[j,i]-20;
            colored[j,i,2] = img[j,i]-30;

im_color = cv2.applyColorMap(img, cv2.COLORMAP_RAINBOW)

plt.subplot(2, 2, 1),plt.imshow(img, 'gray'),plt.title('Original Image') 
plt.subplot(2, 2, 2),plt.imshow(colored),plt.title('Pseudocolored Image using User defined Function')
plt.subplot(2, 2, 3), plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 2, 4),plt.imshow(im_color),plt.title('Pseudocolored Image using Inbuilt Function')
plt.show()
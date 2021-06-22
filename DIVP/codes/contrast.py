import cv2 
import numpy as np 
from matplotlib import pyplot as plt
# Function to map each intensity level to output intensity level. 
def stretch(img, r1, s1, r2, s2): 
    height,width=img.shape
    img1 = np.zeros((height,width),dtype = 'uint8')
    for i in range(width):
        for j in range(height):
            if (img[j,i] <= r1): 
                img1[j,i] = (s1 / r1)*img[j,i]
            elif (r1 < img[j,i] and img[j,i] <= r2): 
                img1[j,i] = ((s2 - s1)/(r2 - r1)) * (img[j,i] - r1) + s1 
            else: 
                img1[j,i] = ((255 - s2)/(255 - r2)) * (img[j,i] - r2) + s2
    img1 = np.array(img1, dtype = np.uint8)
    return img1 
  
# Open the image. 
img = cv2.imread('Images/crow.jpg',0)
  
# Define parameters. 
r1 = 70
s1 = 0
r2 = 140
s2 = 255
  
img2 = stretch(img,r1,s1,r2,s2)

plt.subplot(2, 2, 1),plt.imshow(img, 'gray'),plt.title('Original Image') 
plt.subplot(2, 2, 2),plt.imshow(img2, 'gray'),plt.title('Contrast Stretched Image')
plt.subplot(2, 2, 3), plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 2, 4), plt.hist(img2.ravel(),256,[0,256]),plt.title('Histogram of Contrast Stretched Image')
plt.show()
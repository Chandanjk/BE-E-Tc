import cv2 
  
# import Numpy 
import numpy as np 
from matplotlib import pyplot as plt
# read a image using imread 
img = cv2.imread('Images/babyincradle.png',0) 
  
# creating a Histograms Equalization 
# of a image using cv2.equalizeHist() 
equ = cv2.equalizeHist(img) 
  

a = np.zeros((256,),dtype=np.float16)
b = np.zeros((256,),dtype=np.float16)

height,width=img.shape

#finding histogram
for i in range(width):
    for j in range(height):
        g = img[j,i]
        a[g] = a[g]+1

print(a)   

#performing histogram equalization
tmp = 255/(height*width)

#for i in range(256):
#    for j in range(i+1):
#        b[i] += a[j] * tmp;
#    b[i] = round(b[i] * 255);

b[0]=a[0]*tmp
for i in range(1,256):
    b[i] = b[i-1]+a[i]*tmp;

for i in range(0,256):
    b[i] = round(b[i]);


# b now contains the equalized histogram
#b=b.astype(np.uint8)
b = np.array(b, dtype = np.uint8)
print(b)

#Re-map values from equalized histogram into the image
#As at the end we are getting intensity value to be mapped for that pixel
#just replace that value in the original image with new value(b array)
img1 = np.zeros((height,width),dtype = 'uint8')
for i in range(width):
    for j in range(height):
        g = img[j,i]
        img1[j,i]= b[g]

plt.subplot(2, 3, 1),plt.imshow(img, 'gray'),plt.title('Original Image') 
plt.subplot(2, 3, 2),plt.imshow(equ, 'gray'),plt.title('Histogram Equilized Image(inbuilt function)')
plt.subplot(2, 3, 3),plt.imshow(img1, 'gray'),plt.title('Histogram Equilized Image(user defined function)')
plt.subplot(2, 3, 4),plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram Original Image')
plt.subplot(2, 3, 5),plt.hist(equ.ravel(),256,[0,256]),plt.title('Histogram of Image equilized using inbuilt function')
plt.subplot(2, 3, 6),plt.hist(img1.ravel(),256,[0,256]),plt.title('Histogram of Image equilized using User defined function')
plt.show()



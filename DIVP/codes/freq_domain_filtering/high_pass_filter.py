import cv2 
import numpy as np 
from matplotlib import pyplot as plt
import math

img = cv2.imread('./Images/lotus.jpg', 0) # gray-scale image
img = img[:500, :500] # crop to 500 x 500 

D0=30
#n=1
row, column = img.shape
filter = np.zeros((row,column),dtype = 'uint8')
for i in range(0,row):
    for j in range(0,column):
        D=((i-(row/2))**2+(j-column/2)**2)**0.5        #calculating the distance of point (i,j) from center point
        #filter[i,j]=1/((1+(D0/D)**(2*n)))     #butterworth   
        #filter[i,j]=1-exp(-D/(2*D0*D0))       #gaussian
        if(D<D0):
            filter[i,j]=0
        else:
            filter[i,j]=1     #for ideal

dft = cv2.dft(img.astype(np.float32), flags=cv2.DFT_COMPLEX_OUTPUT)

#Since the center of image does not coincide with the origin
#we have to handle this problem with np.fft.fftshift() function
#What this function does is just divide an image into four small images
#and then rearrange them such that it becomes symmetric about the center.
f_shifted = np.fft.fftshift(dft)
f_complex = f_shifted[:,:,0]*1j + f_shifted[:,:,1]
#applying the filter to the image
f_filtered = filter * f_complex

#taking inverse FT
inv_img = np.fft.ifft2(f_filtered)
filtered_img = np.abs(inv_img)

plt.subplot(3, 2, 1), plt.imshow(img, 'gray'),plt.title('Original Image')
plt.subplot(3, 2, 3), plt.imshow(filtered_img, 'gray'),plt.title('High Pass Filtered Image')
plt.subplot(3, 2, 2), plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(3, 2, 4), plt.hist(filtered_img.ravel(),256,[0,256]),plt.title('Histogram of High Pass Filtered Image')
plt.subplot(3, 2, 5), plt.imshow(filter, 'gray'),plt.title('High Pass Filter')
plt.subplot(3, 2, 6), plt.imshow(filtered_img, 'gray'),plt.title('High Pass Filtered Image')
plt.show()
# -*- coding: utf-8 -*-
import cv2 
  
# import Numpy 
import numpy as np 
from matplotlib import pyplot as plt

def low_pass(img):
    #filter design
    Do = 50 #value of Cutoff freq Do
    ham = np.hamming(256)[:,None] # 1D hamming
    ham2d = np.sqrt(np.dot(ham, ham.T)) ** Do # expand to 2D hamming
    print("HAM = ",ham);
    print("HAM2d = ",ham2d);
    #Transforming the image to freq domain, output has 2 parts: real and imaginary
    dft = cv2.dft(img.astype(np.float32), flags=cv2.DFT_COMPLEX_OUTPUT)
    #Since the center of image does not coincide with the origin
    #we have to handle this problem with np.fft.fftshift() function
    #What this function does is just divide an image into four small images
    #and then rearrange them such that it becomes symmetric about the center.
    f_shifted = np.fft.fftshift(dft)
    f_complex = f_shifted[:,:,0]*1j + f_shifted[:,:,1]

    #applying the filter to the image
    f_filtered = ham2d * f_complex

    #taking inverse FT
    f_filtered_shifted = np.fft.fftshift(f_filtered)
    inv_img = np.fft.ifft2(f_filtered_shifted)
    filtered_img = np.abs(inv_img)
    filtered_img -= filtered_img.min()
    #expand the result such that all values are between 0 and 255
    filtered_img = filtered_img*255 / filtered_img.max()
    #convert back to uint8
    filtered_img = filtered_img.astype(np.uint8)
    return filtered_img;


img = cv2.imread('./Images/lenna.jpg', 0) # gray-scale image
img = img[:500, :500] # crop to 500 x 500 
filtered_img = low_pass(img)

plt.subplot(2, 2, 1), plt.imshow(img, 'gray'),plt.title('Original Image')
plt.subplot(2, 2, 2), plt.imshow(filtered_img, 'gray'),plt.title('Low Pass Filtered Image')
plt.subplot(2, 2, 3), plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 2, 4), plt.hist(filtered_img.ravel(),256,[0,256]),plt.title('Histogram of Low Pass Filtered Image')
plt.show()
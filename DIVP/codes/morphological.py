import cv2 
  
# import Numpy 
import numpy as np 
from matplotlib import pyplot as plt

# read a image using imread 
img = cv2.imread('Images/morphological/ero_dila.png',0)
img1 = cv2.imread('Images/morphological/open_close.png',0)

# Taking a matrix of size 5 as the kernel 
kernel = np.ones((5,5), np.uint8) 
open_kernel = np.ones((45,45), np.uint8)
close_kernel = np.ones((30,30), np.uint8)
def opening(img,kernel):
    img_ero = cv2.erode(img, kernel, iterations=1) 
    img_open = cv2.dilate(img_ero, kernel, iterations=1)
    return img_open

def closing(img,kernel):
    img_dil = cv2.dilate(img, kernel, iterations=1) 
    img_close = cv2.erode(img_dil, kernel, iterations=1)
    return img_close

# The first parameter is the original image, 
# kernel is the matrix with which image is  
# convolved and third parameter is the number  
# of iterations, which will determine how much  
# you want to erode/dilate a given image.  
img_erosion = cv2.erode(img, kernel, iterations=1) 
img_dilation = cv2.dilate(img, kernel, iterations=1)
img_opening = opening(img1, open_kernel)
img_closing = closing(img1, close_kernel)

plt.subplot(2, 3, 1),plt.imshow(img, 'gray'),plt.title('Original Image') 
plt.subplot(2, 3, 2),plt.imshow(img_erosion, 'gray'),plt.title('Eroded Image')
plt.subplot(2, 3, 3),plt.imshow(img_dilation, 'gray'),plt.title('Dilated Image')
plt.subplot(2, 3, 4), plt.imshow(img1, 'gray'),plt.title('Original Image')
plt.subplot(2, 3, 5), plt.imshow(img_opening, 'gray'),plt.title('Image Opening')
plt.subplot(2, 3, 6), plt.imshow(img_closing, 'gray'),plt.title('Image Closing')
plt.show()
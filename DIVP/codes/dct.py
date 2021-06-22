from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

# Reading the input image 
img = cv2.imread('Images/hibiscus.tif', 0) 

imf = np.float32(img)  # float conversion
dct1 = cv2.dct(imf)              # the dct
dct = np.uint8(dct1)    # convert back to int

idct = cv2.idct(dct1)         # take idct

error = imf - idct

idct = np.uint8(idct)  #convert back to int
error = np.uint8(error)

plt.subplot(2, 3, 1),plt.imshow(img, 'gray'),plt.title('Original Image') 
plt.subplot(2, 3, 2),plt.imshow(dct, 'gray'),plt.title('DCT of Image')
plt.subplot(2, 3, 3),plt.imshow(idct, 'gray'),plt.title('IDCT of Image')
plt.subplot(2, 3, 4), plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Original Image')
plt.subplot(2, 3, 5), plt.hist(dct.ravel(),256,[0,256]),plt.title('Histogram of DCT of Image')
plt.subplot(2, 3, 6), plt.hist(idct.ravel(),256,[0,256]),plt.title('Histogram of IDCT of Image')
plt.show()

plt.imshow(error , cmap=plt.cm.gray)
plt.title("Error between original and after taking IDCT")
plt.show()
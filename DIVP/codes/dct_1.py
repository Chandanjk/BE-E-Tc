from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import scipy
import scipy.fftpack
from numpy import pi
from numpy import sin
from numpy import zeros
from numpy import r_
from scipy import signal
from scipy import misc # pip install Pillow
import matplotlib.pylab as pylab

# import math module 
import math

def get_DCT(img):
    h, w = img.shape
    out = np.zeros((h,w),dtype = 'uint8')
    Temp=0
    AlphaP=0;
    AlphaQ=0;
    cs1=0;
    cs2=0;
    for i in range(0,w):
        for j in range(0,h):
            if(j==1):
                AlphaP=math.sqrt(1/h);
            else:
                AlphaP=math.sqrt(2/h);
            if(i==1):
                AlphaQ=math.sqrt(1/w);
            else:
                AlphaQ=math.sqrt(2/w);
            
            for x in range(0,w):
                for y in range(0,w):
                    cs1=math.cos((pi*(2*x-1)*(i-1))/(2*w));
                    cs2=math.cos((pi*(2*y-1)*(j-1))/(2*h));
                    Temp=Temp+(img[y,x]*cs1*cs2);
            out[j,i]=AlphaP*AlphaQ*Temp;
    return out;

#def dct2(a):
#   return scipy.fftpack.dct( scipy.fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )

#def idct2(a):
#    return scipy.fftpack.idct( scipy.fftpack.idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')

def part_A_dct(img):
    h, w = img.shape
    imf = np.float32(img)
    out = np.zeros((h,w))
    for i in range(0,h,8):
        for j in range(0,w,8):
            out[i:(i+8), j:(j+8)] = cv2.dct(imf[i:(i+8), j:(j+8)])
    dct = np.uint8(out) 
    return dct

def part_A_idct(img1):
    h, w = img1.shape
    imf = np.float32(img)
    out = np.zeros((h,w))
    for i in range(0,h,8):
        for j in range(0,w,8):
            out[i:(i+8), j:(j+8)] = cv2.idct(imf[i:(i+8), j:(j+8)])
    idct = np.uint8(out)
    return idct


# Reading the input image 
img = cv2.imread('Images/dct.tif', 0) 
img = cv2.resize(img,(800,800))
out_dct = part_A_dct(img)

thresh = 0.012
dct_thresh = out_dct * (abs(out_dct) > (thresh*np.max(out_dct)))

out_idct = part_A_idct(out_dct)         # take idct

error = img - out_idct

plt.subplot(3, 2, 1), plt.imshow(img, 'gray'),plt.title('Original Image')
plt.subplot(3, 2, 2), plt.imshow(out_dct, 'gray'),plt.title('DCT')
plt.subplot(3, 2, 3), plt.imshow(dct_thresh, 'gray'),plt.title('Thresholded')
plt.subplot(3, 2, 4), plt.imshow(out_idct, 'gray'),plt.title('IDCT')
plt.subplot(3, 2, 5), plt.imshow(error, 'gray'),plt.title('error')
plt.show()
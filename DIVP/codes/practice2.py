import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('Images/hist1.bmp',0)
plt.hist(img1.ravel(),256,[0,256]) 
plt.show()

img2 = cv2.imread('Images/hist2.bmp',0)
plt.hist(img2.ravel(),256,[0,256]) 
plt.show()
import cv2
import numpy as np
from matplotlib import pyplot as plt

def global_threshold(img,T,delta):
    # Find width and height of image
    row, column = img.shape
    G1=0;
    G2=0;
    g1=0;
    g2=0;
    Tnew = 0;
    img1 = np.zeros((row, column),dtype = 'uint8')
    while 1:
        G1=0;
        G2=0;
        g1=0;
        g2=0;
        for i in range(row):
            for j in range(column):
                if img[i,j]>T:
                    G1+=img[i,j];
                    g1+=1;
                else:
                    G2+=img[i,j];
                    g2+=1;
        Tnew = ((G1/g1)+(G2/g2))/2;
        if(abs(T-Tnew) < delta):
            break;
        else:
            T=Tnew;
    print(T);
    for i in range(row):
        for j in range(column):
            if img[i,j]>T:
                img1[i,j] = 255;
            else:
                img1[i,j] = 0;
    return img1;

# Load the image
img = cv2.imread('images/threshold.jpg',0)

deltaT = 2
T = 127

out = global_threshold(img,T,deltaT)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print(ret)

adaptive_thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 19, 3)

adaptive_thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 19, 3)

# Display the image
plt.subplot(2, 3, 1), plt.imshow(img, 'gray'),plt.title('Original image')
plt.subplot(2, 3, 2), plt.imshow(out, 'gray'),plt.title('Global Thresholded Image using User defined function')
plt.subplot(2, 3, 3), plt.imshow(th1, 'gray'),plt.title('Global Thresholded Image using inbuilt function')
plt.subplot(2, 3, 4),plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Original image')
plt.subplot(2, 3, 5),plt.hist(out.ravel(),256,[0,256]),plt.title('Histogram of Thresholded image using user defined function')
plt.subplot(2, 3, 6),plt.hist(th1.ravel(),256,[0,256]),plt.title('Histogram of Thresholded image using inbuilt function')
plt.show()

plt.subplot(2, 2, 1), plt.imshow(adaptive_thresh1, 'gray'),plt.title('Adaptive Mean Thresholded image')
plt.subplot(2, 2, 2), plt.imshow(adaptive_thresh2, 'gray'),plt.title('Adaptive Gaussian Thresholded image')
plt.subplot(2, 2, 3),plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Mean Thresholded image')
plt.subplot(2, 2, 4),plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram of Adaptive Thresholded image')
plt.show()

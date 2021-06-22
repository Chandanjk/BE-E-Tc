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

def Adaptive_Threshold(img):
    row, column = img.shape
    intImg = np.zeros((row, column),dtype = 'uint8')
    Aout = np.zeros((row, column),dtype = 'uint8')
    sum=0
    s=abs(row/8)
    t=15
    for i in range(row):
        sum = 0
    for j in range(column):
        sum = sum+img[i, j]
    if i == 0:
        intImg[i, j] = sum
    else:
        intImg[i, j] = intImg[i-1, j] + sum

    for i in range(row):
        for j in range(column):
            x1 = (int)(i - s/2)
            x2 = (int)(i + s/2)
            y1 = (int)(j - s/2)
            y2 = (int)(j + s/2)
            count = (x2-x1)*(y2-y1)
            sum = intImg[x2,y2]-intImg[x2,y1-1]-intImg[x1-1,y2]+intImg[x1-1,y1-1]
            if (img[i, j]*count) <= (sum*(100-t)/100):
                Aout[i, j] = 0
            else:
                Aout[i, j] = 255
    return Aout;


# Load the image
img = cv2.imread('images/threshold.jpg',0)

deltaT = 2
T = 127

out = global_threshold(img,T,deltaT)
out1 = global_threshold(img,T,deltaT)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print(ret)
# Display the image
plt.subplot(2, 4, 1), plt.imshow(img, 'gray'),plt.title('Original image')
plt.subplot(2, 4, 2), plt.imshow(out, 'gray'),plt.title('Global Thresholding')
plt.subplot(2, 4, 3), plt.imshow(th1, 'gray'),plt.title('Global Thresholding using inbuilt')
plt.subplot(2, 4, 4), plt.imshow(out1, 'gray'),plt.title('Adaptive Thresholding')
plt.subplot(2, 4, 5),plt.hist(img.ravel(),256,[0,256])
plt.subplot(2, 4, 6),plt.hist(out.ravel(),256,[0,256])
plt.subplot(2, 4, 7),plt.hist(th1.ravel(),256,[0,256])
plt.subplot(2, 4, 8),plt.hist(out1.ravel(),256,[0,256])
plt.show()

import cv2 
import numpy as np 
from matplotlib import pyplot as plt  

a = [0,0,0,6,14,5,0,0]
b = np.zeros((8,),dtype=np.float16)

print(a)   

tmp = 7/25

b[0]=a[0]*tmp
for i in range(1,8):
    b[i] = b[i-1]+a[i]*tmp;

for i in range(0,8):
    b[i] = round(b[i]);


# b now contains the equalized histogram
b=b.astype(np.uint8)

print(b)



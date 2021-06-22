import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Images/dove1.jpg',0)
m, n = img.shape 
# empty list to store the count  
# of each intensity value 
count =[] 
# empty list to store intensity  
# value 
r = [] 
# loop to traverse each intensity  
# value 
for k in range(0, 256): 
    r.append(k) 
    count1 = 0
    # loops to traverse each pixel in  
    # the image  
    for i in range(m): 
        for j in range(n): 
            if img[i, j]== k: 
                count1+= 1
    count.append(count1) 

plt.subplot(1, 2, 1),plt.stem(r, count),plt.xlabel('intensity value'),plt.ylabel('number of pixels'),plt.title('Histogram using user defined method') 
plt.subplot(1, 2, 2),plt.hist(img.ravel(),256,[0,256]),plt.title('Histogram Using Inbuilt Function')
plt.show()

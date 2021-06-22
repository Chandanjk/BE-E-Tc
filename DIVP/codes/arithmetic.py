import cv2 
import numpy as np 
from matplotlib import pyplot as plt
# read a image using imread 
img1 = cv2.imread('Images/Arithmetic/ar1.png',0)
img2 = cv2.imread('Images/Arithmetic/ar2.png',0)

addn = cv2.add(img1, img2)
subn = cv2.subtract(img1, img2)
andn = cv2.bitwise_and(img1,img2, mask = None)
orn = cv2.bitwise_or(img1,img2, mask = None)
xorn = cv2.bitwise_xor(img1,img2, mask = None)
notn = cv2.bitwise_not(img1, mask = None)

plt.subplot(3,3,1),plt.imshow(img1, 'gray'),plt.title('Image 1')
plt.subplot(3,3,2),plt.imshow(img2, 'gray'),plt.title('Image 2')
plt.subplot(3,3,4),plt.imshow(addn, 'gray'),plt.title('Addition Operation')
plt.subplot(3,3,5),plt.imshow(subn, 'gray'),plt.title('Subtraction Operation')
plt.subplot(3,3,6),plt.imshow(andn, 'gray'),plt.title('Logical AND Operation')
plt.subplot(3,3,7),plt.imshow(orn, 'gray'),plt.title('Logical OR Operation')
plt.subplot(3,3,8),plt.imshow(xorn, 'gray'),plt.title('Logical XOR Operation')
plt.subplot(3,3,9),plt.imshow(notn, 'gray'),plt.title('Logical NOT Operation(Image 1)')
plt.show()
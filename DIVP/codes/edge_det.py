import cv2
import numpy as np
import matplotlib.pyplot as plt
 
image = cv2.imread('Images/laplacian/coin.jpg',0)
image = cv2.resize(image,(800,600))

 # Robertsedge operator
kernel_Roberts_x = np.array([
    [1, 0],
    [0, -1]
    ])
kernel_Roberts_y = np.array([
    [0, -1],
    [1, 0]
    ])
 # Sobel edge operator
kernel_Sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]])
kernel_Sobel_y = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]])
 # Prewitt edge operator
kernel_Prewitt_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]])
kernel_Prewitt_y = np.array([
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]])
  
kernel_Laplacian_point = np.array([
    [0, 1, 0],
    [1, -8, 1],
    [0, 1, 0]])
kernel_Laplacian_horizontal = np.array([
    [-1,-1,-1],
    [2, 2, 2],
    [-1,-1,-1]])

kernel_Laplacian_45 = np.array([
    [-1, -1, 2],
    [-1, 2, -1],
    [2, -1, -1]])
kernel_Laplacian_neg_45 = np.array([
    [2, -1, -1],
    [-1, 2, -1],
    [-1, -1, 2]])
kernel_Laplacian_vertical = np.array([
    [-1, 2, -1],
    [-1, 2, -1],
    [-1, 2, -1]])

 # convolution

output_laplacian_point = cv2.filter2D(image, -1, kernel_Laplacian_point)
output_laplacian_horizontal = cv2.filter2D(image, -1, kernel_Laplacian_horizontal)
output_laplacian_45 = cv2.filter2D(image, -1, kernel_Laplacian_45)
output_laplacian_neg_45 = cv2.filter2D(image, -1, kernel_Laplacian_neg_45)
output_laplacian_vertical = cv2.filter2D(image, -1, kernel_Laplacian_vertical)
output_Roberts_x = cv2.filter2D(image, -1, kernel_Roberts_x)
output_Roberts_y = cv2.filter2D(image, -1, kernel_Roberts_y)
output_prewitt_x = cv2.filter2D(image, -1, kernel_Prewitt_x)
output_prewitt_y = cv2.filter2D(image, -1, kernel_Prewitt_y)
output_sobel_x = cv2.filter2D(image, -1, kernel_Sobel_x)
output_sobel_y = cv2.filter2D(image, -1, kernel_Sobel_y)

output_Roberts = output_Roberts_x + output_Roberts_y
output_prewitt = output_prewitt_x + output_prewitt_y
output_sobel = output_sobel_x + output_sobel_y

plt.subplot(3, 3, 1), plt.imshow(image, 'gray'),plt.title('Original image')
plt.subplot(3, 3, 2), plt.imshow(output_laplacian_point, 'gray'),plt.title('Point Detection')
plt.subplot(3, 3, 3), plt.imshow(output_laplacian_horizontal, 'gray'),plt.title('Laplacian Horizaontal')
plt.subplot(3, 3, 4), plt.imshow(output_laplacian_45, 'gray'),plt.title('Laplacian +45')
plt.subplot(3, 3, 5), plt.imshow(output_laplacian_neg_45, 'gray'),plt.title('Laplacian -45')
plt.subplot(3, 3, 6), plt.imshow(output_laplacian_vertical, 'gray'),plt.title('Laplacian Vertical')
plt.subplot(3, 3, 7), plt.imshow(output_Roberts, 'gray'),plt.title('Roberts operator')
plt.subplot(3, 3, 8), plt.imshow(output_prewitt, 'gray'),plt.title('Prewitt operator')
plt.subplot(3, 3, 9), plt.imshow(output_sobel, 'gray'),plt.title('Sobel operator')
plt.show()
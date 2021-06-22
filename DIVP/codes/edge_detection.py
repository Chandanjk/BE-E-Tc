from cv2 import cv2
import numpy as np 
import matplotlib.pyplot as plt 

	
def Zero_crossing(image):
    z_c_image = np.zeros(image.shape)
    
    # For each pixel, count the number of positive
    # and negative pixels in the neighborhood
    
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            negative_count = 0
            positive_count = 0
            neighbour = [image[i+1, j-1],image[i+1, j],image[i+1, j+1],image[i, j-1],image[i, j+1],image[i-1, j-1],image[i-1, j],image[i-1, j+1]]
            d = max(neighbour)
            e = min(neighbour)
            for h in neighbour:
                if h>0:
                    positive_count += 1
                elif h<0:
                    negative_count += 1
 
 
            # If both negative and positive values exist in 
            # the pixel neighborhood, then that pixel is a 
            # potential zero crossing
            
            z_c = ((negative_count > 0) and (positive_count > 0))
            
            # Change the pixel value with the maximum neighborhood
            # difference with the pixel
 
            if z_c:
                if image[i,j]>0:
                    z_c_image[i, j] = image[i,j] + np.abs(e)
                elif image[i,j]<0:
                    z_c_image[i, j] = np.abs(image[i,j]) + d
                
    # Normalize and change datatype to 'uint8' (optional)
    z_c_norm = z_c_image/z_c_image.max()*255
    z_c_image = np.uint8(z_c_norm)
 
    return z_c_image

#Read an image
img = cv2.imread('img7.tif',0) 

#Compute laplacian 
laplacian = cv2.Laplacian(img , cv2.CV_64F)
laplacian = Zero_crossing(laplacian)

#compute LoG
blur = cv2.GaussianBlur(img,(3,3),0) #apply gaussian filter first
LoG = cv2.Laplacian(blur,cv2.CV_64F) #apply laplacian on gaussian
LoG = Zero_crossing(LoG)

#compute DoG
blur5 = cv2.GaussianBlur(img,(5,5),0) #apply 5*5 gaussian kernel
blur3 = cv2.GaussianBlur(img,(3,3),0) #apply 3*3 gaussian kernel

DoG = blur5 - blur3 #take the difference to calculate DoG

#apply sobel filter
sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobel_y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

#apply canny edge detection
canny = cv2.Canny(img,100,200) 

#apply prewitt edge detection
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]]) #kernel for x 
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]]) #kernel for y
img_prewittx = cv2.filter2D(img, -1, kernelx)    #apply kernel x
img_prewitty = cv2.filter2D(img, -1, kernely)    #apply kernel y
prewitt = img_prewittx + img_prewitty            #add result of both filters
  
#apply roberts edge detection
roberts_cross_v = np.array( [[ 0, 0, 0 ],[ 0, 1, 0 ],[ 0, 0,-1 ]] ) #vertical roberts kernel
roberts_cross_h = np.array( [[ 0, 0, 0 ],[ 0, 0, 1 ],[ 0,-1, 0 ]] ) #horizontal roberts 
img_roberts_h = cv2.filter2D(img , -1 , roberts_cross_h)
img_roberts_v = cv2.filter2D(img , -1 , roberts_cross_v)
roberts = img_roberts_h+img_roberts_v

# Visualizing img
plt.figure(0)
plt.imshow(img , cmap=plt.cm.gray)
plt.title("Original image")

plt.figure(1)
plt.imshow(laplacian, cmap=plt.cm.gray)
plt.title("Laplacian filter")

plt.figure(2)
plt.imshow(LoG, cmap=plt.cm.gray)
plt.title("LoG filter")

plt.figure(3)
plt.imshow(DoG, cmap=plt.cm.gray)
plt.title("DoG filter")

plt.figure(4)
plt.imshow(canny, cmap=plt.cm.gray)
plt.title("Canny edge detection")

plt.figure(5)
plt.imshow(sobel, cmap=plt.cm.gray)
plt.title("Sobel edge detection")

plt.figure(6)
plt.imshow(prewitt, cmap=plt.cm.gray)
plt.title("Prewitt edge detection")

plt.figure(7)
plt.imshow(roberts, cmap=plt.cm.gray)
plt.title("Robert edge detection")

plt.show()



  

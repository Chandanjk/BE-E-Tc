import matplotlib.pyplot as pyplot
import cv2

path= "Images/hist1.bmp"
#Using matplotlib library
image=pyplot.imread(path)
print(image)
pyplot.imshow(image)
pyplot.show()

#Using cv2 library
image = cv2.imread(path)
print(image)
print(image.shape)
print(type(image))
cv2.imshow("test image",image)
cv2.waitKey(6000)
cv2.destroyAllWindows()
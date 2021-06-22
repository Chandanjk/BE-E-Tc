import numpy as np

#Array
a1 = np.array([1,2,3,4,5,6])
print ("\nArray 1 is : ", a1)

a2 = np.array([6,5,4,3,2,1])
print ("\nArray 2 is : ", a2)

# Printing type of array object
print("Array is of type: ", type(a1)) 
  
# Printing array dimensions (axes) 
print("No. of dimensions: ", a1.ndim) 
  
# Printing shape of array 
print("Shape of array: ", a1.shape) 
  
# Printing size (total number of elements) of array 
print("Size of array: ", a1.size) 
  
# Printing type of elements in array 
print("Array stores elements of type: ", a1.dtype)

m1 = np.array( [[ 1, 2, 3],[ 4, 5, 6]] )
print ("\nMatrix 1 is : ", m1)

m2 = np.array( [[ 6, 5, 4],[ 3, 2, 1]] )
print ("\nMatrix 2 is : ", m2)

# Printing type of matrix object
print("Matrix is of type: ", type(m1)) 
  
# Printing matrix dimensions (axes) 
print("No. of dimensions: ", m1.ndim) 
  
# Printing shape of matrix 
print("Shape of Matrix: ", m1.shape) 
  
# Printing size (total number of elements) of matrix 
print("Size of Matrix: ", m1.size) 
  
# Printing type of elements in matrix 
print("Matrix stores elements of type: ", m1.dtype)

# add arrays 
print ("Array sum:\n", a1 + a2) 
  
# multiply arrays (elementwise multiplication) 
print ("Array multiplication:\n", a1*a2) 
  
# matrix multiplication 
print ("Matrix multiplication:\n", a1.dot(a2)) 

# Creating array from list with type float 
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
print ("Array created using passed list:\n", a) 
  
# Creating array from tuple 
b = np.array((1 , 3, 2)) 
print ("\nArray created using passed tuple:\n", b) 
  
# Creating a 3X4 array with all zeros 
c = np.zeros((3, 4)) 
print ("\nAn array initialized with all zeros:\n", c) 
  
# Create a constant value array of complex type 
d = np.full((3, 3), 6, dtype = 'complex') 
print ("\nAn array initialized with all 6s." 
            "Array type is complex:\n", d) 
  
# Create an array with random values 
e = np.random.random((2, 2)) 
print ("\nA random array:\n", e) 
  
# Create a sequence of integers  
# from 0 to 30 with steps of 5 
f = np.arange(0, 30, 5) 
print ("\nA sequential array with steps of 5:\n", f) 
  
# Create a sequence of 10 values in range 0 to 5 
g = np.linspace(0.5, 5, 10) 
print ("\nA sequential array with 10 values between 0 and 5:\n", g) 
  
# Reshaping 3X4 array to 2X2X3 array 
a = np.array([[1, 2, 3, 4], 
                [5, 2, 4, 2], 
                [1, 2, 0, 1]]) 
  
new = a.reshape(2, 2, 3) 
  
print ("\nOriginal array:\n", a) 
print ("Reshaped array:\n", new) 
  
# Flatten array 
a = np.array([[1, 2, 3], [4, 5, 6]]) 
flarr = a.flatten() 
  
print ("\nOriginal array:\n", a) 
print ("Fattened array:\n", flarr) 


a = np.array([[-1, 2, 0, 4], 
              [4, -0.5, 6, 0], 
              [2.6, 0, 7, 8], 
              [3, -7, 4, 2.0]]) 
print ("\nOriginal array:\n", a)

# Slicing array 
temp = a[:2, ::2] 
print ("Array with first 2 rows and alternate"
                    "columns(0 and 2):\n", temp) 
  
# Integer array indexing example 
temp = a[[0, 1, 2, 3], [3, 2, 1, 0]] 
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
                                    "(3, 0):\n", temp) 
  
# boolean array indexing example 
cond = a > 0 # cond is a boolean array 
temp = a[cond] 
print ("\nElements greater than 0:\n", temp) 

a = np.array([1, 2, 5, 3]) 
print ("\nOriginal array:\n", a)

# add 1 to every element 
print ("Adding 1 to every element:", a+1) 
  
# subtract 3 from each element 
print ("Subtracting 3 from each element:", a-3) 
  
# multiply each element by 10 
print ("Multiplying each element by 10:", a*10) 
  
# square each element 
print ("Squaring each element:", a**2) 
  
# modify existing array 
a *= 2
print ("Doubled each element of original array:", a) 
  
# transpose of array 
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 
  
print ("\nOriginal array:\n", a) 
print ("Transpose of array:\n", a.T)
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

#print("Enter the number of inputs")
#Nx = int(input())

#print("Enter the inputs")
#x = []
#for i in range(Nx):
#    temp.append(float(input("Element:")))
#x = numpy.array(x)
#print("Inputs : "x)

#print("Enter the number of hidden layer units")
#Nz = int(input())

#print("Enter the Weights")
#v = []
#for i in range(0, Nz):
#    b = []
#    print("Enter the Weights for Z",i)
#    for j in range(0, Nx):
#        temp = float(input())
#        b.append(temp)
#    v.append(b)
#v = np.array(v)
#print("Weights : ", v)

x = np.array([1, 0, 1])

v = np.array([
    [0.3, 0.6, -0.1],
    [0.5, -0.3, 0.4]
])

w = np.array([-0.2, 0.4, 0.1])

Ze = np.array([1])

tk = 1

alpha = 0.25

#Feed Forward Stage
#Net Input(HL)
Zin = np.dot(v, x)
print("Zin : ",Zin)

#Apply Activation Function(HL)
z = sigmoid(Zin)
print("z : ",z)

z = np.append(Ze,z)
print("z : ",z)

#Net Input(OL)
yin = np.dot(z, w)
print("yin : ",yin)

#Apply Activation Function(OL)
y = sigmoid(yin)
print("y : ",y)

#Back Propogation of Error
#Error at output layer
Gk = (tk - y)*(y * (1 - y))
print("Gk : ",Gk)

#Error portion in hidden layer
Gin = w * Gk
print("Gin : ",Gin)

l = np.arange(0, Ze.size, 1)
G = np.delete(Gin * (z * (1 - z)),l)
print("G : ",G)

#Weight Updation at output layer
Wnew = w + (alpha * Gk * z)
print("Wnew : ",Wnew)

#Weight Updation at Hidden Layer
Vnew = []
for i in range(0, v.shape[0]):
    b = v[i] + (alpha * G[i] * x)
    Vnew.append(b)
Vnew = np.array(Vnew)
print("Vnew : ",Vnew)
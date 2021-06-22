import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def linear(x):
    return 0.3*x

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def Bipolar_sigmoid(x):
    return (1 - np.exp(-x))/(1 + np.exp(-x))

def tanh(x):
    return 2*sigmoid(2*x) - 1

def relu(x):
    return np.maximum(0,x)

def leaky_relu(x):
    return np.maximum(0.05*x,x)

def swish(x):
    return x/(1 + np.exp(-x))

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

print("Linear(0.64) = ", linear(0.64))
print("sigmoid(0.64) = ", sigmoid(0.64))
print("Bipolar_sigmoid(0.64) = ", Bipolar_sigmoid(0.64))
print("tanh(0.64) = ", tanh(0.64))
print("relu(0.64) = ", relu(0.64))
print("leaky_relu(0.64) = ", leaky_relu(0.64))
print("swish(0.64) = ", swish(0.64))
print("softmax(0.64) = ", softmax(0.64))

x = np.linspace(-10,10,50)
print(x)

p1 = linear(x)
p2 = sigmoid(x)
p3 = Bipolar_sigmoid(x)
p4 = tanh(x)
p5 = relu(x)
p6 = leaky_relu(x)
p7 = swish(x)
p8 = softmax(x)

plt.subplot(4,2,1)
plt.xlabel("x")
plt.ylabel("linear(x)")
plt.plot(x,p1)

plt.subplot(4,2,2)
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.plot(x,p2)

plt.subplot(4,2,3)
plt.xlabel("x")
plt.ylabel("Bipolar Sigmoid(x)")
plt.plot(x,p3)

plt.subplot(4,2,4)
plt.xlabel("x")
plt.ylabel("Tanh(x)")
plt.plot(x,p4)

plt.subplot(4,2,5)
plt.xlabel("x")
plt.ylabel("Relu(x)")
plt.plot(x,p5)

plt.subplot(4,2,6)
plt.xlabel("x")
plt.ylabel("Leaky_Relu(x)")
plt.plot(x,p6)

plt.subplot(4,2,7)
plt.xlabel("x")
plt.ylabel("Swish(x)")
plt.plot(x,p7)

plt.subplot(4,2,8)
plt.xlabel("x")
plt.ylabel("Softmax(x)")
plt.plot(x,p8)

plt.show()
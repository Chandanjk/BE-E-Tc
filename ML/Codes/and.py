import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

w1 = 1
w2 = 1
bias = 1
threshold = np.linspace(-5,5,1000)

x1 = np.array([1, 1, 0, 0])
#print("x1 = ",x1)

x2 = np.array([1, 0, 1, 0])
#print("x2 = ",x2)

z = np.array([1, 0, 0, 0])
#print("z = ",z)

yin = w1*x1 + w2*x2 + bias
#print("yin = ",yin)

for i in threshold:
    y = np.where(yin > i, 1, 0)
    #print("y = ",y)
    if(np.array_equal(y, z)):
        print("For Threshold = ",i,"we get y : ",y,"= z : ",z)
        break;
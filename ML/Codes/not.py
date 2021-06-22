import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

w = 1
bias = 1
threshold = np.linspace(-5,5,1000)

x = np.array([1, 1, 0, 0])
#print("x1 = ",x1)

z = np.array([0, 0, 1, 1])
#print("z = ",z)

yin = w*x + bias
#print("yin = ",yin)

for i in threshold:
    y = np.where(yin > i, 1, 0)
    #print("y = ",y)
    if(np.array_equal(y, z)):
        print("For Threshold = ",i,"we get y : ",y,"= z : ",z)
        break;
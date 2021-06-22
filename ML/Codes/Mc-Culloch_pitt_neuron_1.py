import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("Enter the coice of Gate :\n1 : AND Gate\n2 : OR Gate\n3 : NOT Gate\n4 : XOR Gate")
c = int(input())
input_table = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1],
])
threshold = np.linspace(-5,5,1000)
if c==1:
    print("Enter the weights :\nw1 = ")
    w1 = int(input())
    print("w2 = ")
    w2 = int(input())
    print("bias = ")
    bias = int(input())

    z = np.array([0, 0, 0, 1])
    #print("z = ",z)
    weights = np.array([w1,w2])
    yin = input_table @ weights + bias
    #print("yin = ",yin)

    for i in threshold:
        y = np.where(yin > i, 1, 0)
        #print("y = ",y)
        if(np.array_equal(y, z)):
            print("For Threshold = ",i,"we get y : ",y,"= z : ",z)
            break
elif c==2:
    print("Enter the weights :\nw1 = ")
    w1 = int(input())
    print("w2 = ")
    w2 = int(input())
    print("bias = ")
    bias = int(input())
    
    z = np.array([0, 1, 1, 1])
    #print("z = ",z)
    weights = np.array([w1,w2])
    yin = input_table @ weights + bias
    #print("yin = ",yin)

    for i in threshold:
        y = np.where(yin > i, 1, 0)
        #print("y = ",y)
        if(np.array_equal(y, z)):
            print("For Threshold = ",i,"we get y : ",y,"= z : ",z)
            break
elif c==3:
    print("Enter the weights :\nw = ")
    #In case of NOT gate we will have to use inhibitory weight(which contribute to negayive values of inputs) to get proper threshold.
    w = int(input())
    print("bias = ")
    bias = int(input())
    
    x = np.array([0, 1])
    #print("x1 = ",x1)

    z = np.array([1, 0])
    #print("z = ",z)

    yin = w*x + bias
    #print("yin = ",yin)

    for i in threshold:
        y = np.where(yin > i, 1, 0)
        #print("y = ",y)
        if(np.array_equal(y, z)):
            print("For Threshold = ",i,"we get y : ",y,"= z : ",z)
            break
elif c==4:
    print("Enter the weights :\nw1 = ")
    w1 = int(input())
    print("w2 = ")
    w2 = int(input())
    print("bias = ")
    bias = int(input())
    threshold = np.linspace(-5,5,1000)
else:
    print("\nPlease enter Proper Option")     
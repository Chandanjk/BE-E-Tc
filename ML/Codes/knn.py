import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

x = [[0],[1],[2],[3]]

y = [0,0,1,1]

neigh = KNeighborsClassifier(n_neighbors=3)

neigh.fit(x,y)

print(neigh.predict([[2.1]]))
print(neigh.predict([[1.1]]))
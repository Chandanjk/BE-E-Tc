import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier 
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Dataset1.csv')
print(df)
#convert string data into float
lab = LabelEncoder()
df['Outlook'] = lab.fit_transform(df['Outlook'])
df['Temp'] = lab.fit_transform(df['Temp'])
df['Humidity'] = lab.fit_transform(df['Humidity'])
df['Windy'] = lab.fit_transform(df['Windy'])
df['Play'] = lab.fit_transform(df['Play'])

#convert to numpy
a=df.to_numpy()

cols=df.columns
x_train = a[:,0:cols.size-1]
y_train = a[:,cols.size-1]

cn = ['yes' , 'no']

#print(x_train);
#print(y_train.shape);


classifier = DecisionTreeClassifier(criterion='entropy')  
classifier = classifier.fit(x_train, y_train)  
tree.plot_tree(classifier,feature_names=cols[0:cols.size-1] , class_names=cn,filled=True)
plt.show()
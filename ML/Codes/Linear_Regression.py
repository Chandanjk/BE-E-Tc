import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Boston hdata.csv')
print(df)

print(df.head())

df = pd.read_csv('Boston hdata.csv',delim_whitespace=True, header= None)
print(df)

print(df.head())

cols = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PIRATIO','B','LSTAT','MEDV']
df.columns = cols

print(df.head())

print("Description : \n",df.describe())

print("Correlation : \n",df.corr())

#sns.pairplot(df,height=1.5)
#plt.show()

#col_study = ['CRIM','RM','MEDV','LSTAT']
#sns.pairplot(df[col_study],height=3.5)
#plt.show()

#plt.figure(figsize=(16.10))
#sns.heatmap(df.corr(),annot=True)
#plt.show()

a=df.to_numpy()
cols=df.columns
x = a[:,0:cols.size-1]
y = a[:,cols.size-1]

model = LinearRegression()
model.fit(x,y)

print("slope = ",model.coef_)
print("intercept = ",model.intercept_)

#plt.figure(figsize=(8,8))
#sns.regplot(x,y)
#plt.xlabel('average number of rooms per ')
#plt.ylabel('Median value of owner-occupied homes in 1000$s')
#plt.show()

sns.jointplot(x='MEDV',y='RM',data=df,kind='reg',height=10)
plt.show()

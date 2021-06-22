import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from matplotlib import style
style.use("ggplot")
from sklearn.svm import SVC

x,y = make_blobs(n_samples=250,centers=2,random_state=0,cluster_std=0.60)
y[y==0]=-1
tmp=np.ones(len(x))
y=tmp*y
plt.scatter(x[:,0],x[:,1],c=y,cmap='winter')
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)

clf = SVC(kernel='linear', C = 1.0).fit(x_train,y_train)

print(clf.predict(x_test))
#print(clf.predict([10.58]))

w = clf.coef_[0]
b = clf.intercept_[0]
print(w)

xx = np.linspace(-4,4)
yy = (-w[0] * xx - b) / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(x_train[:,0],x_train[:,1],c=y_train,cmap='winter')
plt.legend()
plt.show()
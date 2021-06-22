import numpy as np
import cvxopt
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.svm import SVC

iris = datasets.load_iris()
# Take the first two features. We could avoid this by using a two-dim dataset
x = iris.data
y = iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)

#training a linear SVM model
svm_linear_model = SVC(kernel='linear', C = 1.0).fit(x_train,y_train)
svm_predictions = svm_linear_model.predict(x_test)
print(svm_predictions)

#model accuracy for x_test
accuracy = svm_linear_model.score(x_test, y_test)
print(accuracy)

#creating confusion matrix
cm = confusion_matrix(y_test, svm_predictions)
print(cm)
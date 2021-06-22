import numpy as np
from matplotlib import pyplot as plt  

x = np.array([1,2,3,4,5])
y = np.array([3,4,2,4,5])

mean_x = np.mean(x)
mean_y = np.mean(y)

numerator = 0
denominator = 0

for i in range(x.size):
    numerator += (x[i] - mean_x)*(y[i] - mean_y)
    denominator += (x[i] - mean_x)**2

m = numerator/denominator

c = mean_y - (m * mean_x)

print("\nsolpe = ",m)
print("\nintercept = ",c)
print("\nLine fitted : y =",m,"x +",c)

y_predicted = np.zeros(y.size)

for i in range(x.size):
    y_predicted[i] = (m * x[i]) + c

print("\nx = ",x)
print("\ny = ",y)
print("\ny_predicted = ",y_predicted)

numerator = 0
denominator = 0

for i in range(x.size):
    numerator += (y_predicted[i] - y[i])**2
    denominator += (y[i] - mean_y)**2

R_sq_coeff = numerator/denominator

print("\nR_square Coefficient = ",R_sq_coeff)

plt.scatter(x,y)
plt.plot(x,y_predicted,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Predicted and Original Y')
plt.show()
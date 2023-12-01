import numpy as np
import matplotlib.pyplot as plt

X = [0,1,2,3]
Y = [0,3,1,2]

x = np.linspace(0,3,100)
y = np. zeros_like(x)


X3 =[X[0]**3, X[0]**2, X[0], 1], [X[1]**3, X[1]**2, X[1], 1], [X[2]**3, X[2]**2, X[2], 1], [X[3]**3, X[3]**2, X[3], 1]

A = np.linalg.inv(X3)@Y

print(A)

for i in range(len(y)):
    y[i] = A[0] * pow(x[i], 3) + A[1] * pow(x[i],2) + A[2]*x[i] + A[3]



plt.plot(X,Y, "o")
plt.figure()
plt.plot(x,y,"o")
plt.show()
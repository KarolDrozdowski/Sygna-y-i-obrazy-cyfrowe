import numpy as np
import matplotlib.pyplot as plt

X = [0,1,2]
Y = [0,3,0]

x = np.linspace(0,2,10)
y = np. zeros_like(x)


X2 = [X[0]**2, X[0], 1],[X[1]**2, X[1], 1],[X[2]**2, X[2], 1]

A = np.linalg.inv(X2)@Y

print(A)

for i in range(len(y)):
    y[i] = A[0] * pow(x[i], 2) + A[1] * x[i] + A[2]

print(y)

plt.plot(X,Y, "o")
plt.figure()
plt.plot(x,y,"o")
plt.show()
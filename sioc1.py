import numpy as np
import matplotlib.pyplot as plt

###interpolacja metodą najbliższego sąsiada
def najblizszySasiad (X,Y,x1):
    y1 = np.zeros_like(x1)
    i = 0
    j = 0
    for xi in x1:
        if xi-X[j] < X[j+1]-xi:
            y1[i] = Y[j]
        else:
            y1[i] = Y[j+1]
        if xi >= X[j+1]:
            j +=1
        i +=1
    return y1

###interpolacja liniowa
def linearInterpolation(X,Y,x1):
    y1=np.zeros_like(x1)
    i = 0
    j=0
    for xi in x1:
        y1[i] = Y[j] + ((xi-X[j])*(Y[j+1]-Y[j]) / (X[j+1]-X[j]))
        i +=1

        if xi > X[j+1]:
            j +=1

    return y1

###interpolacja kwadratowa
def quadraticInterpolation (X, Y, x1):
    y1=np.zeros_like(x1)
    i=0
    j=0
    for xi in x1:
        X2 = [X[j] ** 2, X[j], 1], [X[j+1] ** 2, X[j+1], 1], [X[j+2] ** 2, X[j+2], 1]
        Y2=[Y[j], Y[j+1], Y[j+2]]
        A = np.linalg.inv(X2) @ Y2
        y1[i] = A[0] * pow(xi, 2) + A[1] * xi + A[2]
        i+=1

        if xi > X[j+2]:
            j+=1
    return y1


###tworzymy nasze tablice, X,Y tworzy wykres sinusa, x1 słuzy do interpolacji
X = np.linspace(0,5, 10)
Y = np.sin(X)
x1 = np.linspace(0,5, 100)


###wyswietlanie wykresow
plt.plot(X,Y, "o")
plt.title("Wykres sin, dane poczatkowe")

plt.figure()
plt.plot(x1, najblizszySasiad (X,Y,x1), "o")
plt.title("Interpolacja metoda najblizszego sasiada")

plt.figure()
plt.plot(x1, linearInterpolation(X,Y,x1), "o")
plt.title("Linear interpolation")

plt.figure()
plt.plot(x1, quadraticInterpolation(X,Y,x1), "o")
plt.title("Quadratic interpolation")

plt.show()
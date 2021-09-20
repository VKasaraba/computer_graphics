import matplotlib.pyplot as plt
from math import cos, sin, log

x = lambda t: 5*(cos(t) - t*sin(t)) + log(t) + 20*cos(t/4)
y = lambda t: 5*(sin(t) + t*cos(t)) - log(t) + 20*sin(t/4)

h = 0.1
t = 1
top = 20
bottom = 1

X_points = []
Y_points = []

while bottom <= round(t, 1) <= top:
    X_points.append(x(t))
    Y_points.append(y(t))
    t += h

plt.plot(X_points, Y_points)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
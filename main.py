import math
import matplotlib.pyplot as plt
import numpy as np


def throwingParabola(v, ss):
    print("Throwing Parabola")
    g = 9.81  # gravitational acceleration
    t = np.linspace(0, 2 * v * math.sin(ss) / g, 100)

    def x(t):
        return v * t * math.cos(ss)

    def y(t):
        return v * t * math.sin(ss) - g / 2 * t ** 2

    return x, y


# Path: main.py-----------------------------------
print("See the following graphic:")

x, y = throwingParabola(10, 45)
t = np.linspace(0, 2 * 10 * math.sin(45) / 9.81, 100)   # t = Numpy array
xs = [x(t_i) for t_i in t]
ys = [y(t_i) for t_i in t]
plt.plot(xs, ys)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

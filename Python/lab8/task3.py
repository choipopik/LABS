import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

figure = plt.figure()

r = np.linspace(0, 1, 202)
t = np.linspace(-5, 5, 100)


def animation(i):
    figure.clear()
    i += 1
    x = np.sin(t)
    y = np.sin(r[i] * t)
    plt.plot(x, y)


anim = FuncAnimation(figure, animation, frames=200, interval=10)
plt.show()

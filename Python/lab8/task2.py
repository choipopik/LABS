import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-1, 1, 1000)
a = np.array([3, 3, 5, 5])
b = np.array([2, 4, 4, 6])

A = 100
B = 100
d = np.pi / 2

fig, ax = plt.subplots(2, 2)

x1 = A * np.sin(a[0] * t + d)
y1 = B * np.sin(b[0] * t)
ax[0, 0].plot(x1, y1)
ax[0, 0].set_title('3:2')

x2 = A * np.sin(a[1] * t + d)
y2 = B * np.sin(b[1] * t)
ax[0, 1].plot(x2, y2)
ax[0, 1].set_title('3:4')

x3 = A * np.sin(a[2] * t + d)
y3 = B * np.sin(b[2] * t)
ax[1, 0].plot(x3, y3)
ax[1, 0].set_title('5:4')

x4 = A * np.sin(a[3] * t + d)
y4 = B * np.sin(b[3] * t)
ax[1, 1].plot(x4, y4)
ax[1, 1].set_title('5:6')

plt.show()

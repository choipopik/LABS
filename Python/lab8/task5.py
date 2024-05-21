import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 2, subplot_kw={'projection': '3d'})

x1 = np.linspace(0, 10, 100)
y1 = np.random.normal(0, 1, 100)
z1 = np.square(y1)

x2 = np.linspace(0, 10, 100)
y2 = np.random.normal(0, 1, 100)
z2 = np.square(y2)

ax[0].plot_trisurf(x1, y1, z1)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_zlabel('z')

ax[1].plot_trisurf(x2, y2, z2)
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[1].set_zlabel('z')
ax[1].set_zscale('log')

plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

amp1 = 5
fq1 = 2

fig, ax = plt.subplots(3, 1)


x1 = np.linspace(-10, 10, 500)
y1 = amp1*np.sin(fq1 * x1)
line1, = ax[0].plot(x1, y1)

ax_fq1 = plt.axes([0.1, 0.9, 0.1, 0.1])
fq1 = Slider(ax_fq1, 'fq1', valmin=0, valmax=10)

ax_amp1 = plt.axes([0.3, 0.9, 0.1, 0.1])
amp1 = Slider(ax_amp1, 'amp1', valmin=0, valmax=10)


x2 = np.linspace(-10, 10, 500)
y2 = np.cos(x2)
line2, = ax[1].plot(x2, y2)

ax_fq2 = plt.axes([0.6, 0.9, 0.1, 0.1])
fq2 = Slider(ax_fq2, 'fq2', valmin=0, valmax=10)

ax_amp2 = plt.axes([0.8, 0.9, 0.1, 0.1])
amp2 = Slider(ax_amp2, 'amp2', valmin=0, valmax=10)


line3, = ax[2].plot(x1 + x2, y1 + y2)


def update(val):
    n_fq1 = fq1.val
    n_amp1 = amp1.val
    line1.set_ydata(n_amp1*np.sin(n_fq1 * x1))

    n_fq2 = fq2.val
    n_amp2 = amp2.val
    line2.set_ydata(n_amp2*np.sin(n_fq2 * x2))

    line3.set_ydata(n_amp1*np.sin(n_fq1 * x1) + n_amp2*np.sin(n_fq2 * x2))


fq1.on_changed(update)
amp1.on_changed(update)

fq2.on_changed(update)
amp2.on_changed(update)

plt.show()

import matplotlib.pyplot as plt
import numpy as np
import scipy.special

def leg_pol_func(x,n):
    func = scipy.special.legendre(n)
    result = func(x)
    return result
N = 1000

x = np.linspace(-1,1,N)
y1 = leg_pol_func(x,1)
y2 = leg_pol_func(x,2)
y3 = leg_pol_func(x,3)
y4 = leg_pol_func(x,4)
y5 = leg_pol_func(x,5)
y6 = leg_pol_func(x,6)
y7 = leg_pol_func(x,7)

plt.title("Полиномы Лежандра")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)
plt.plot(x, y6)
plt.plot(x, y7)
plt.show()
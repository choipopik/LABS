import numpy as np

# Задание 6

a6 = np.arange(16).reshape(4, 4)  # orig. array
print(a6, '\n')
a6[[0, 2]] = a6[[2, 0]]  # swapped array
print(a6)

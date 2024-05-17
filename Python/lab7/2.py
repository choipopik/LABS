import numpy as np

# Задание 2

x = np.array([2, 2, 2, 3, 3, 3, 5])
result = np.unique(x, return_counts=True)
print(result)
import numpy as np

# Задание 2

x = np.array([2, 2, 2, 3, 3, 3, 5])

qnt = np.unique(x)
reps = np.diff(x)
print(qnt, reps)

import numpy as np

# Задание 4

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
nul = np.array([])
dif_x = np.diff(x)
for i in range(1, len(x) - 1):
    if x[i] == dif_x[i - 1]:
        nul = np.append(nul, x[i])
print(np.max(nul))

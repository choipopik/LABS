import numpy as np

# Задание 1
mtx = np.loadtxt("file.txt", delimiter=',')
print(f'Сумма: {np.sum(mtx)}, максимальный эл-т: {np.max(mtx)}, минимальный эл-т: {np.min(mtx)}')

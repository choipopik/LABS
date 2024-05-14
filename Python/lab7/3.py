import numpy as np

# Задание 3

a = np.random.normal(size=(10, 4))
print(f'Минимальное:{a.min()}, максимальное:{a.max()}, среднее:{a.mean()}, стандартное отклонение:{a.std()}', '\n')
first_five = a[5:]
print(first_five)

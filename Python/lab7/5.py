import numpy as np
import time
import scipy
from scipy.stats import multivariate_normal

X = np.array([[1, 3], [3, 7]])
C = np.array([[1, 0.5], [0.5, 2]])
M = np.array([0, 0])

start1 = time.perf_counter()
func = scipy.stats.multivariate_normal(M, C).logpdf(X)
finish1 = time.perf_counter()
duration1 = finish1 - start1

start2 = time.perf_counter()  # Засекаем начало
logpdf = -0.5 * (np.log(2 * np.pi) + np.log(np.linalg.det(C)) + np.einsum('ij,ij->i', X - M, np.dot(np.linalg.inv(C), X - M)))  # Своя функция вычисления
finish2 = time.perf_counter()  # Засекаем конец
duration2 = finish2 - start2
# print(logpdf)
# print(duration2)


print("Значение реализованной функции:", logpdf)
print("Значение функции scipy:", func)
print('Разница значений:', logpdf - func)
print('Разница времени вычисления:', duration1 - duration2)

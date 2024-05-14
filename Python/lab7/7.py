import numpy as np

# Задание 7

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
uniq = np.array([])
for i in range(0, 150):
    if iris[i][4] not in uniq:
        uniq = np.append(uniq, iris[i][4])

# Please don`t mind the 'FutureWarning' sign ^_^
print(uniq, '\n', len(uniq))

def bubble(lst, i):
    tmp = lst[i]
    lst[i] = lst[i + 1]
    lst[i + 1] = tmp


line = input()
to_del = ',.!?:;"()'
for x in to_del:
    line = line.replace(x, '')
line = line.split()
keys = set(line)
n_keys = list(keys)
values = [line.count(x) for x in keys]
for i in range(len(n_keys) - 1):
    for j in range(len(n_keys) - 1 - i):
        if values[j] < values[j + 1]:
            bubble(n_keys, j)
            bubble(values, j)
        elif values[j] == values[j + 1] and n_keys[j] > n_keys[j+1]:
            bubble(n_keys, j)
            bubble(values, j)

for j in range(len(n_keys)):
    print(n_keys[j])

n = int(input())
m = []
for i in range(n):
    m.append(input())
dictionary = {x : m.count(x) for x in m}
for k in dictionary.values():
    print(k)
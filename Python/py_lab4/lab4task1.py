n = int(input())
m = []
d = []
result = 0
for i in range(n):
    m.append(input())
for x in m:
    if x not in d:
        d.append(x)

print(len(d))
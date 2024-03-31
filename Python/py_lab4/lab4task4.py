string = "one two     one two  three two"
d = string.split(" ")
i = 0
m = []
while i < len(d):
    if d[i] == "":
        del d[i]
        i -= 1
    else:
        i += 1

print(d)

for i in range(len(d)):
    print(m.count(d[i]))
    m.append(d[i])

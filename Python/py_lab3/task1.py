s = input()
k = []
j = 1
p = ""
for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        p += s[i]
    elif len(p) > 0 and s[i] != s[i + 1]:
        k.append(p[0] + str(len(p) + 1))
        p = ""
    else:
        k.append(s[i])
if len(p) > 0:
    k.append(p[0] + str(len(p) + 1))
if s[-1] != s[-2]:
    k.append(s[-1])
print(*k, sep="")

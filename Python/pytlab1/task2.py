# task 2
d = int(input())
s = ""
i = 0
jd = len(str(d))
while d > 0:
    i += 1
    s += str(i) + (" " * (jd - len(str(i))))
    print(s)
    d -= 1

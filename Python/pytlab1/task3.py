# task 3
d = int(input()) - 1
s = "1"
i = 1
jd = len(str(d+1))
print((d * " ") + s)
while d > 0:
    i += 1
    std_ots = (" " * (d - 1))
    s = str(i) + s + str(i)
    print(std_ots + s)
    d -= 1
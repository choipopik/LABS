## task 3
#    d = int(input()) - 1
#    s = "1"
#    i = 1
#    jd = len(str(d+1))
#    print((d * " ") + s)
#    while d > 0:
#        i += 1
#        std_ots = (" " * (d - 1))
#        s = str(i) + s + str(i)
#        print(std_ots + s)
#        d -= 1
d = int(input())
k = d
for i in range(d+1):
    print(" " * k, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for l in range(2, i+1):
        print(l, end="")
    k -= 1
    print()



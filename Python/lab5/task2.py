inpt = open("input2.txt")
outpt = open("output2.txt","w")
m = []
for i in range (10):
    l = inpt.readline().strip("\n")
    m.append(int(l))
m = sorted(m)
for i in m:
    outpt.write(str(i)+" ")

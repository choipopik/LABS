inpt = open("input3.txt")
outpt_max = open("output3max.txt","w")
outpt_min = open("output3min.txt","w")
data = []
vozrast = []
for l in inpt:
    m = l.split()
    data.append(m)
    vozrast.append(int(m[2]))
for x in data:
    if int(x[2]) == max(vozrast):
        outpt_max.write(x[0]+" "+x[1]+" "+x[2])
    elif int(x[2]) == min(vozrast):
        outpt_min.write(x[0]+" "+x[1]+" "+x[2])



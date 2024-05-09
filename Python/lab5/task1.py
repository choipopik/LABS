inpt = open("input1.txt")
outpt = open("output1.txt","w")
l = inpt.readline().split()
result = 1
for i in l:
    result *= int(i)
print(result)
outpt.write(str(result))
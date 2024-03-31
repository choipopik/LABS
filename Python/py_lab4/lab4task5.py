def purch_sum(lst):
    summa = 0
    for x in lst:
        summa += int(x[1])
    return summa


n = int(input())
purchases = {}
for i in range(n):
    stroka = input()
    data = stroka.split()
    id = int(data[0])
    prod = data[1]
    quant = int(data[2])

    if id in purchases:
        purchases[id].append((prod, quant))
    else:
        purchases[id] = [(prod, quant)]

for key, value in purchases.items():
    print("id", key, ":", "Всего покупок", purch_sum(value))
    for x in value:
        print(x[0], "-", x[1])

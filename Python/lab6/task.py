import csv
import random
import os


def Show(dir, dig, data):
    if dig == '':
        dig = 5
    dig = int(dig)

    if len(data) - 1 < 5:
        dir = 'top'
        print('Строк недостаточно')

    lines_lenghts = []
    for i in range(0, len(data[0])):
        one_line = []
        for j in range(0, dig):
            one_line.append(len(str(data[j][i])))
        lines_lenghts.append(one_line)

    if dir == 'top' or dir == '':
        for i in range(0, dig + 1):
            for j in range(0, len(data[0])):
                print(str(data[i][j]).center(max(lines_lenghts[j])), end=' ')
            print("\n")

    if dir == 'bottom':
        data.append(data[0])
        for i in reversed(range(len(data) - dig - 1, len(data))):
            for j in range(0, len(data[0])):
                print(str(data[i][j]).center(max(lines_lenghts[j])), end=' ')
            print("\n")

    if dir == 'random':
        rrdata = random.sample(data[1:], dig)
        rrdata.insert(0, data[0])
        for i in range(0, dig + 1):
            for j in range(0, len(data[0])):
                print(str(rrdata[i][j]).center(max(lines_lenghts[j])), end=' ')
            print("\n")


def data_type(strg):
    try:
        int(strg)
        return 'int'
    except:
        pass
    try:
        float(strg)
        return 'float'
    except:
        pass
    return 'string'


def Info(data):
    print(f'{len(data) - 1}x{len(data[0])}')
    for i in range(len(data[0])):
        qnt = 0
        k = 1
        dtype = ''
        for j in range(len(data) - 1):
            if data_type(data[j][i]) == 'float':
                dtype = 'float'
            if data[j][i] != '':
                qnt += 1
                dbtype = data_type(data[j][i])

        if dtype != 'float': dtype = dbtype

        print(data[0][i], qnt, dtype)


def DelNaN(data):
    cleaned = []
    for i in range(0, len(data)):
        if '' not in data[i]:
            cleaned.append(data[i])
    return cleaned


def MakeDS(data):
    data70 = []
    data30 = []
    num = int((len(data) - 1) * 0.7)
    rdata = random.sample(data[1:], len(data) - 1)
    os.makedirs('workdata/learning')
    os.makedirs('workdata/testing')
    train = open('workdata/learning/train.csv', 'w', newline='')
    test = open('workdata/testing/test.csv', 'w', newline='')
    writer70 = csv.writer(train)
    writer30 = csv.writer(test)
    writer70.writerow(data[0])
    writer30.writerow(data[0])
    for i in range(num):
        writer70.writerow(rdata[i])
    for j in range(num, len(data) - 1):
        writer30.writerow(rdata[j])

file = open('Titanic.csv', 'r')
_data = list(csv.reader(file, delimiter=','))
# MakeDS(_data)
# Info(_data)
# Show('bottom', 3, _data)
# DelNaN(_data)

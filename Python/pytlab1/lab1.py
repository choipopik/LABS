# task 1
def match(a, b, c):
    data = [a, b, c]
    matches = []
    for i in range(len(data)):
        matches.append(data.count(data[i]))
    if max(matches) == 1:
        return 0
    else:
        return max(matches)


a = input()
b = input()
c = input()
print(match(a, b, c))

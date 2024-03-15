s = input() + "/"
result = []
tmp = ""
d_tmp = "0"
i = 0
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(0, len(s)):
    if s[i] in digits:
        d_tmp += s[i]
    else:
        result.append(tmp * int(d_tmp))
        result.append(s[i])
        tmp = s[i]
        d_tmp = "0"
while '' in result:
    result.remove('')
for i in range(0, len(result) - 1):
    if result[i] == result[i + 1][0]:
        result[i] = ""
result.remove('/')
print(*result, sep="")

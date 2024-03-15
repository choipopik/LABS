s = input()
words = s.split()
result =''
for i in range(len(words)):
    result+=words[i][0].upper()
print(result)
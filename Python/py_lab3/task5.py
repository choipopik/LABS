def func(mat):
    for i in range(2):
        if mat[0][i] / mat[0][i + 1] == mat[1][i] / mat[1][i + 1] == mat[2][i] / mat[2][i + 1]:
            return ("столбцы линейно зависимы")
    return ("столбцы линейно независимы")


# mat = [
#     [1, 2, 3],
#     [4, 8, 6],     <- матрица с л.зав. столбцами
#     [7, 14, 8]
# ]

# mat = [
#     [10, 20, 30],
#     [40, 50, 60],    <- матрица с лин.незав. столбцами
#     [70, 80, 80]
# ]

n = 3
matr = []
for i in range(n):
    strok = []
    for j in range(n):
        strok.append(int(input()))
    matr.append(strok)

print(func(matr))

for i in range(n):
    print (matr[i])

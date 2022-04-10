matrizA = [[10, 14, 0, 7],
            [5, 17, 5, 2],
            [17, 8, 1, 2],
            [2, 0, 14, 0],
            [8, 7, 8, 3]
            ]

# troca o elemento do 1º índice pelo 3º índice
for i in range(5):
    aux = matrizA[i][0]
    matrizA[i][0] = matrizA[i][2]
    matrizA[i][2] = aux
print(matrizA)

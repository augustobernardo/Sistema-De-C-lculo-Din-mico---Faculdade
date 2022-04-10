
def cria_matriz(m, n):
    # cria uma matriz de Mxn
    return [[0] * n for i in range(m)]

# passa os parâmetros para M e N
a = cria_matriz(5, 5)

for i in range(5):
    # linhas
    for j in range(5):
        # colunas
        if i < j and (j % 2):
            # adicionando os valores da matriz
            a[i][j] = i+j

print(a)

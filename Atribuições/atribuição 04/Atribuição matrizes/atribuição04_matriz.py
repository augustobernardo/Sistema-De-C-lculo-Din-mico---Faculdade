# objetivo 1: imprimir a soma dos elementos da primeira coluna da matriz
# objetivo 2: imprimir a soma dos elementos da diagonal principal
# objetivo 3: imprimir a soma dos elementos acima da diagonal principal
# objetivo 4: calcular e imprimir a soma de todos os elementos, exceto a diagonal principal.
# objetivo 5: imprimir apenas os números negativos da matriz.


def inicio():
    # criando a matriz
    matriz = [
            [1, 7, 8, 10], 
            [-3, 6, -9, 11], 
            [5, -4, 2, 0] , 
            [12, 3, -8, 9]]

    # transpondo a matriz
    """matriz_transposta = [
            [1, -3, 5, 12], 
            [7, 6, -4, 3], 
            [8, -9, 2, -8], 
            [10, 11, 0, 9]]"""      
    # somando a primeira linha da matriz_transposta (pois a linha da transposta == coluna da matriz normal)
    #soma_primeiraColuna = int(matriz_transposta[0][0]) +  int(matriz_transposta[0][1]) + int(matriz_transposta[0][2]) + int(matriz_transposta[0][3])

    somaPrimeiraColuna(matriz)
    somaDiagonalPrincipal(matriz)
    somaElementosAcima(matriz)
    somaTodosElementos(matriz)
    numerosNegativos(matriz)


# Calculando a soma dos valores da primeira coluna
def somaPrimeiraColuna(matriz):
    # acessando a primeira coluna da matriz
    soma_primeiraColuna = matriz[0][0] + matriz[1][0] + matriz[2][0] + matriz[3][0]

    """
    Ou usar a matriz transposta -> matriz_transposta[0][1] + matriz_transposta[0][2] + matriz_transposta[0][3]
    """

    print(f'A soma da primeira coluna da matriz dada é de: {soma_primeiraColuna}\n')


# Calculando a diagonal principal
def somaDiagonalPrincipal(matriz):
    # acessando a diagonal
    diagonal_principal = matriz[0][0] + matriz[1][1] + matriz[2][2] + matriz[3][3]
    print(f'A soma da diagonal principal é de: {diagonal_principal}\n')


# Calculando a soma dos elementos acima da diagonal
def somaElementosAcima(matriz):
    # somando as linhas e depois somando os resultados
    elementos_acima = (matriz[0][1] + matriz[0][2] + matriz[0][3]) + (matriz[1][2] + matriz[1][3]) + (matriz[2][3])
    #                     soma dos elementos da primeira linha               segunda linha           terceira linha

    print(f'A soma dos elementos acima da diagonal principal é de: {elementos_acima}\n')


# Calculando todos os elementos eceto a diagonal
def somaTodosElementos(matriz):
    # calculando a soma das linhas e somando os resultados
    todos_elementos = ((matriz[0][1] + matriz[0][2] + matriz[0][3]) + # soma da primeira linha
                        (matriz[1][0] + matriz[1][2] + matriz[1][3]) + # soma da segunda
                        (matriz[2][0] + matriz[2][1] + matriz[2][3]) + # soma da terceira
                        (matriz[3][0] + matriz[3][1] + matriz[3][2]) # soma da quarta
                    )

    print(f'A soma de todos os elementos execto a diagonal é de: {todos_elementos}\n')


# Imprimindo apenas os números negativos
def numerosNegativos(matriz):
    # imprimindo apenas os números negativos
    print(f'O números negativos dessa matriz são:\n')

    # Percorre linha por linha da matriz
    for linha in range(len(matriz)):
        # elemento -> variável para ver cada valor dentro da linha 
        for elemento in range(len(matriz[0])):
            if matriz[linha][elemento] < 0:
                print(f'Na {linha}º linha: {matriz[linha][elemento]}')

if __name__ == '__main__':
    inicio()

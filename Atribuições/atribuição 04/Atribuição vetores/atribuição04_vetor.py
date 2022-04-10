# objetivo 1: adicionar os itens dinamicamente -> exemplo de output: v = [1, -5, 0, 3, 9, -1, 7]
# objetivo 2: calcular a soma dos valores do vetor
# objetivo 3: somar os valores de v[0], v[3] e v[6] e imprimir o resultado
# objetivo 4: somar os índices pares e índices ímpares do vetor

v = []
soma = 0
soma_indices = 0
soma_par = 0
soma_impar = 0
somaTotal = 0

for i in range(7):
    pergunta = int(input(f'Digite o número da posição {i}\n>> '))
    # adicionando os valores digitados pelo usuário
    v.append(pergunta)

    # calculando a soma
    soma = soma + v[i]
    # segunda forma de calcular a soma dos valores do vetor
    # soma = soma + pergunta

    # calculando a soma dos índices pares com os índices ímpares
    soma_indices += i

    # calculando a soma dos valores pares e ímpares do vetor
    if (v[i] % 2) == 0:
        soma_par += v[i]

    elif (v[i] % 2) == 1:
        soma_impar += v[i]
print('-' * 35)

# calculando a soma dos valores dos índices 0, 3 e 6
soma_objetiva = v[0] + v[3] + v[6]

# calculando a soma total dos pares com os ímpres
somaTotal = soma_par + soma_impar

# imprimindo o vetor
print(f'O vetor ficou da seguinte forma: {v}\n')
# imprimindo a soma dos valores digitados
print(f'A soma dos valores digitados é de: {soma}\n')
# imprimindo a soma dos valores específicos
print(f'A soma dos valores\nV[0] = {v[0]}\nV[3] = {v[3]}\nV[6] = {v[6]}\né igual a: {soma_objetiva}\n')
# imprimindo a soma dos índices pares com os índices ímpares do vetor
print(f'A soma dos índices pares com os índices ímpares é de: {soma_indices}\n')
# imprimindo a soma dos valores pares com os valores ímpares do vetor
print(f'A soma dos valores pares com os valores ímpares do vetor\nSoma pares: {soma_par}\nSoma ímpares: {soma_impar}\né igual a: {somaTotal}\n')


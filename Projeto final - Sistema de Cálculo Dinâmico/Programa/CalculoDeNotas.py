# Este é um programa que recebe as notas de um número X de alunos em uma matriz, após issom cria um vetor para guardar o nome de cada aluno. Logo depois, fará o cálculo da média de cada aluno
# e imprimirá na tela as notas deste aluno e sua média. Por fim, o programa irá calcular a média da sala toda (a média de todas as notas inseridas para cada aluno) e imprimirá na tela a média
# da sala.

imprimeLinhas = '=' * 40
print(imprimeLinhas)
print('CALCULO DE NOTAS - SALESIANO'.center(40))
print(imprimeLinhas)
separacao = '*' + '=' * 40 + '*'
linha_normal = '-' * 40

# Recebendo os valores de entrada do tipo inteiros para calcular a matriz
pergunta = int(input('Quantos alunos serão inseridos no sistema?\n>> '))
pergunta_notas = int(input('Quantas notas serão atribuidas para cada um dos alunos?\n>> '))

# Criando a matriz
def cria_matriz(linhas, colunas):
    # criando a matriz de linhas x colunas
    m = [[0] * colunas for i in range(linhas)]
    # Criando um vetor para guardar os nomes dos alunos
    v = []

    print('\n')
    for i in range(pergunta):
        nome = str(input(f'Digite o nome do {i + 1}º aluno(a): ')).title()
        v.append(nome)

    # Chamando a função de adiçãodas notas, para preencher a matriz
    adcNotas(linhas, colunas, m, v)

# Adicionando as notas dos alunos
def adcNotas(linhas, colunas, m,v):
    # Adicionando as notas dos alunos nas matrizes
    print('\n')
    for i in range(linhas):
        for j in range(colunas):
            notas = float(input(f'Digite a nota do aluno(a) {v[i]}\n>> '))
            m[i][j] = notas
        print(linha_normal)

    # Imprimindo as notas dos Alunos
    print('')
    print('NOTAS'.center(40))
    print(linha_normal)
    for i in range(linhas):
        print(f'As notas do aluno(a) {v[i]} foram: ')
        for j in range(colunas):
            # Acessando a matriz na linha i (do aluno i) e imprimindo todos os valores passados
            print(f'| {m[i][j]}', end=" | ")
        print("\n")
        print(linha_normal)

    # Chamando a função para calcular as notas dos alunos
    print('')
    print('MÉDIAS'.center(40))
    print(separacao)
    calcularNotas(linhas, colunas, m, v)

# Função para calcular as notas dos alunos
def calcularNotas(linhas, colunas, m, v):
    # Calculando a nota dos alunos
    soma_notas = 0
    for i in range(linhas):
        # limpando o valor da soma para somar novos valores do príxmo aluno
        soma_notas = 0
        for j in range(colunas):
            # Somando todos os valores da linha i
            soma_notas += m[i][j]
        # Calculando a média dos valores somados na linha i 
        media_nota = soma_notas / colunas

        # Verificando se o aluno está reprovado, se vai precisar de fazer a prova final ou se está aprovado
        # se a nota for menor do que 5, então o aluno está reprovado
        if media_nota < 5:
            print(f'A média do aluno(a) {v[i]} foi de: {media_nota:.1f} \n', end=" ")
            print(f'O aluno(a) {v[i]} está reprovado(a)!!')
        # se a nota for maior do que 5 e menor do que 7 (se estiver no intervalo de 5 e 7) então o aluno precisará fazer a prova final
        elif media_nota > 5 and media_nota < 7:
            print(f'A média do aluno(a) {v[i]} foi de: {media_nota:.1f} \n', end=" ")
            print(f'O aluno(a) {v[i]} precisará de fazer a prova final!!\n')
        # se a nota for maior do que 7, então o aluno está aprovado
        elif media_nota > 7:
            print(f'A média do aluno(a) {v[i]} foi de: {media_nota:.1f} \n', end=" ")
            print(f'O aluno(a) {v[i]} está aprovado (a)!!\n')

        # Imprimindo a média do aluno i
        #print(f'A média do aluno(a) {v[i]} foi de: {media_nota:.1f} \n', end=" ")
        print("")
        print(separacao)
    # Chamando a função para calcular a média de todos os alunos listados
    calcMediaSala(linhas, colunas, m, v)

def calcMediaSala(linhas, colunas, m, v):
    # Calculando a média da sala inteira
    soma_sala = 0
    for i in range(linhas):
        for j in range(colunas):
            soma_sala += m[i][j]

    # Calculando a média de todos os alunos listados
    media_sala = soma_sala / (linhas * colunas)

    print('')
    print('MÉDIA DA SALA'.center(40))
    print(separacao)
    # Imprimindo o valor da média de todos os alunos listados
    print(f'A média das notas de todos os alunos inseridos foi de: \n | {media_sala:.2f} |')
    print(separacao)

if __name__ == '__main__':
    cria_matriz(pergunta, pergunta_notas)

linhas = "-" * 20
# Pegando o nome do aluno
nome__aluno = str(input("\nDigite o nome do aluno: "))
# Pegando as notas do aluno
num__notas = int(input(f"\nQuantas notas serão inseridas?\n>> "))
# Criando a variável nota__modificada para usa-lá depois
nota__modificada = 0

# laço de repetição: para i até o número de notas que irá ser digitada
for i in range(num__notas):
    # Pergunta a nota do aluno
    nota__aluno = float(input(f"\nDigite a nota do aluno(a) {nome__aluno}: "))
    # Cada vez que se repetir irá somar: nota__modificada = nota__modificada(anterior) + nota__aluno
    nota__modificada += nota__aluno

# Quando a estrutura de repetição acabar irá calcular a média do aluno:
# Todas as notas somadas dividido pela quantidade de notas inseridas
media__aluno = nota__modificada / num__notas

# Condicionais: Se a media for maior ou igual a 0 e a media menor do que 5 faça
if media__aluno >= 0 and media__aluno < 5:
    print(linhas + "\n")
    print(f'A média do aluno(a) {nome__aluno} foi de {media__aluno:.1f}\n\n{nome__aluno} está \033[4;31mreprovado(a)!!\033[m')

# Condicionais: Se a media for maior ou igual a 5 e a media menor do que 7 faça
elif media__aluno >= 5 and media__aluno < 7:
    print(linhas + "\n")
    print(f'A média do aluno(a) {nome__aluno} foi de {media__aluno:.1f}\n\n{nome__aluno} terá que fazer a \033[4;33mprova especial (recuperação)!!\033[m')

# Condicionais: Se a media for maior ou igual a 7 faça
elif media__aluno >= 7:
    print(linhas + "\n")
    print(f'A média do aluno(a) {nome__aluno} foi de {media__aluno:.1f}\n\n{nome__aluno} está \033[4;32maprovado(a)!!\033[m')


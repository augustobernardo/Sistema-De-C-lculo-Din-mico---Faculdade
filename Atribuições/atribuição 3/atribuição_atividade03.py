linhas = "-" * 20

# função para iniciar o programa e para auxiliar na "limpeza" dos dados anteriores
def inicio():
    nome__aluno = str(input("\nDigite o nome do aluno: ")).title()
    num__notas = int(input(f"\nQuantas notas serão inseridas?\n>> "))
    nota__modificada = 0

    # chamando a função para calcular e receber as notas
    notas(num__notas, nota__modificada, nome__aluno)

# função para calcular as notas
def notas(num__notas, nota__modificada, nome__aluno):
    pergunta = str('N')
    while pergunta == 'N':
        for i in range(num__notas):
            # Pergunta a nota do aluno
            nota__aluno = float(input(f"\nDigite a nota do aluno(a) {nome__aluno}: "))
            # Cada vez que se repetir irá somar: nota__modificada = nota__modificada(anterior) + nota__aluno
            nota__modificada += nota__aluno
        # calculando a média
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

        print(linhas)
        # Perguntando se a pessoa deseja inserir novas informações
        pergunta = str(input(f'Deseja inserir novas informações?\n[S]Sim\n[N]Não\n>> ')).upper()
        # se a resposta for não, então irá acabar o programa
        if pergunta == 'N':
            break
    else:
        # se a resposta da pergunta for sim, então irá chamar a função inicio, limpando todas as informações anteriores
        inicio()

if __name__ == '__main__':
    # quando o programa iniciar irá chamar a função
    inicio()
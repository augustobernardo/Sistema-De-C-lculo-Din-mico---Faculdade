nome = str(input('Digite o nome do aluno: ')).title()
pergunta = str()
c = int()
media = float()

while pergunta != 'N':
    nota = float(input(f'Digite a nota do aluno(a) {nome}: '))
    pergunta = str(input(f'Deseja inserir mais notas?\n[S]Sim\n[N]Não\n>> ')).upper()
    media = nota + media
    c += 1
media_nota = media / c
print(f'A média do aluno(a) {nome} foi de {media_nota}')
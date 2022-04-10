n1 = float(0)
n2 = float(0)
n3 = float(0)


def ler_numeros():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    print(f'Os números lidos foram: {n1}, {n2} e {n3}')

    calcular_soma(n1, n2, n3)

def calcular_soma(a, b, c):
    soma = float(a + b + c)
    print(f'A soma é: {soma}')

    calcular_media(a, b, c)

def calcular_media(a, b, c):
    media = (a + b + c) / 3
    print(f'A média é: {media:.2f}')


if __name__ == '__main__':
    ler_numeros()
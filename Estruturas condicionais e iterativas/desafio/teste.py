numero = int(input('Digite um número: '))
soma = int(0)
divisor = int(1)

while divisor > (numero / 2):
    resto = numero % divisor
    if soma == 0:
        soma = soma + divisor
        print(f'Divisor: {divisor}')
    divisor = divisor + 1
if soma == numero:
    print('Número perfeito')
else:
    print('Número não é perfeito')
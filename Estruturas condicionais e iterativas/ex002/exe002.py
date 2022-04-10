""" numero = int()
divisor = int()
soma = int()
resto = int() 
l = int()

    ALTERNATIVA A
for l in range (1, 1000 + 1):
    soma = 0
    divisor = 1
    numero = l
    while divisor > (numero / 2):
        resto = numero % divisor
        if resto == 0:
            soma = soma + divisor
        divisor = divisor + 1
    if soma == numero:
        print(f'Número Perfeito: {numero}') 
"""


""" 
    #ALTERNATIVA B
numero = int(input('Digite um número: '))
soma = int(0)
divisor = int(1)

while divisor > (numero / 2):
    resto = numero % divisor
    if resto == 0:
        soma = divisor
        print(f'Divisor: {divisor}')
    divisor = divisor + 1
if soma == numero:
    print(f'Número Perfeito')
else:
    print('Não é um número perfeito') 
"""


"""     #ALTERNATIVA C
numero = int(input('Digite um número: '))
soma = int(0)
divisor = int(1)

while (divisor > (numero / 2)):
    resto = numero % divisor
    if resto == 0:
        soma = soma + divisor
        print(f'Divisor: {divisor}')
    divisor = divisor + 1
if soma == numero:
    print(f'Número Perfeito')
else:
    print('Não é um número perfeito')
"""

""" 
    #ALTERNATIVA D
numero = int(input('Digite um número: '))
soma = int(0)
divisor = int(1)

while  (divisor > (numero / 2)):
    resto = numero % divisor
    if (resto != 0):
        soma = soma + divisor
        print(f'Divisor: {divisor}')
    divisor = divisor + 1
if soma == numero:
    print('Número Perfeito')
else:
    print('Não é um número perfeito')
"""


    # ALTERNATIVA CORRETA
    #ALTERNATIVA E
numero = int(input('Digite um número: '))
soma = int(0)
divisor = int(1)

while divisor < numero:
    resto = numero % divisor
    if resto == 0:
        soma = soma + divisor
        print(f'Divisor: {divisor}')
    divisor = divisor + 1
if soma == numero:
    print('Número Perfeito')
else:
    print('Não é um número perfeito')
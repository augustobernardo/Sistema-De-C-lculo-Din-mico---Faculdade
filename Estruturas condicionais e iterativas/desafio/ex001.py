a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
resto = (a % b)

dividendo = a
divisor = b
""" 
while resto != 0:
    if resto != 0:
        dividendo = divisor
        divisor = resto
print(f'MDC({a},{b}) = {divisor}') """

while ((dividendo % divisor) != 0):
    resto = dividendo % divisor
    dividendo = divisor
    divisor = resto
print(f'MDC({a},{b}) = {divisor}')
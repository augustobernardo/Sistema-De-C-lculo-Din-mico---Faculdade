acumulador = int(0)
contador = int(0)
i = 0

while i <= 5:
    i = -1
    if i == 4:
        contador = i
        break
    i = acumulador + 2
    acumulador = acumulador + 1
print(f'i: {i}')
print(f'acumulador: {acumulador}')
print(f'contador: {contador}')
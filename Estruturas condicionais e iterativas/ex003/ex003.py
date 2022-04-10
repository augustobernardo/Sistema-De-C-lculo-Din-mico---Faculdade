inicial = float(input('Digite a massa inicial: '))
final = float()
tempo = int()

final = inicial
tempo = 0

while final < 0.5:
    if final >= 0.5:
        final = final / 2
        tempo = tempo + 50
print(f'Massa inicial: {inicial}'
        f'\nMassa Final: {final}'
        f'\nTempo: {tempo}')

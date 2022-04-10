
x = int(1)
y = int()
z = int()

while ((x > 0) and (x <= 1000)):
    x = int(input('Digite um número inteiro entre 0 e 1000: '))
y = 1000
while y != 0:
    z = x / y
    x = x % y
    y = y / 10
    print(z)
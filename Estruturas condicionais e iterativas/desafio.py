clientes = int(0)
quant_desconto = float(0)
soma_descontos = float(0)
compras = 1

while compras != 0:
    compras = float(input('Digite o valor da compra: R$'))

    if compras > 1000:
        desconto = compras + (compras * (10 / 100))
        print(f'O valor do desconto foi de: R${desconto}')
        print(f'-' * 30)
    elif compras > 500 and compras < 1000:
        desconto = compras + (compras * (5 / 100))
        print(f'O valor do desconto foi de: R${desconto}')
        print(f'-' * 30)
        
    soma_descontos += desconto
    quant_desconto += 1
    clientes += 1

else:
    clientes -= 1
    quant_desconto -= 1
    soma_descontos -= desconto
    print('-' * 30)
    print(f'O número de descontos concedidos foi de: {quant_desconto}')
    print(f'A soma dos descontos foi de: R${soma_descontos}')

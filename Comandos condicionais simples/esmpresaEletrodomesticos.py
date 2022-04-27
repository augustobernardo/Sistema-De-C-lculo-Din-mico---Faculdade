funcionario = str(input('Digite o nome do funcionário: ')).title()
salario_fixo = float(input(f'Digite o salário do funcionário(a) {funcionario}: '))
venda_mensal = float(input(f'Digite qual foi o valor de vendas mensais do(a) {funcionario}: '))


if venda_mensal > 100000.00:
    comissao = 5000.00
    salario_final = salario_fixo + comissao

    print(f'O salário final do(a) {funcionario} é de: R${salario_final:.2f}')
    print(f'A comissão do(a) {funcionario} é de: R${comissao:.2f}')
elif venda_mensal > 55000.00 and venda_mensal <= 100000.00:
    comissao = venda_mensal * (2 / 100)
    salario_final = salario_fixo + comissao

    print(f'O salário final do(a) {funcionario} é de: R${salario_final:.2f}')
    print(f'A comissão do(a) {funcionario} é de: R${comissao:.2f}')
elif venda_mensal < 55000.00:
    comissao = 100.00
    salario_final = salario_fixo + comissao

    print(f'O salário final do(a) {funcionario} é de: R${salario_final:.2f}')
    print(f'A comissão do(a) {funcionario} é de: R${comissao:.2f}')

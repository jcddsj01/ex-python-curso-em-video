cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' AUMENTOS MÚLTIPLOS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    aumento = salario + (salario * (15 / 100))
else:
    aumento = salario + (salario * (10 / 100))
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, aumento))

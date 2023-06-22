cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' REAJUSTE SALARIAL '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

salario = float(input('Qual é o salário do Funcionário? R$ '))
aumento = 15
aumento_salario = salario + (salario * aumento / 100)
print('Um funcionário que ganhava R$ {:.2f}, com {}% de aumento, passa a receber R$ {:.2f}'.format(salario, aumento, aumento_salario))

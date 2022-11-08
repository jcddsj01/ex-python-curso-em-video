cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'vermelho': '\033[1;41m',
    'verde': '\033[1;42m',
    'amarelo': '\033[1;43m',
    'azul': '\033[1;44m',
    'roxo': '\033[1;45m',
    'azulclaro': '\033[1;46m',
    'cinza': '\033[1;47m'
}

print('+', '-' * 8, '+')
print('| {} EX-013 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

salario = float(input('Qual é o salário do Funcionário? R$'))
aumento = 15
aumento_salario = salario + (salario * aumento / 100)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(salario, aumento, aumento_salario))
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
print('| {} EX-015 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

dias_alugados = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))
total_pagar = (dias_alugados * 60) + (km_rodados * 0.15)
print('O total a pagar é de R${:.2f}'.format(total_pagar))
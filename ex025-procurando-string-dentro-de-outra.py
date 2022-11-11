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
print('| {} EX-025 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

nome = str(input('Qual é seu nome completo? ')).strip()

#O operador 'in' verifica se o operando a sua esquerda,
#está contido na lista a sua direita, da mesma forma que
#o operador not in que verifica o contrário.
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

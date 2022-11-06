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
print('| {} EX-002 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

#nome = input('Digite seu nome: ')
#print('É um prazer te conhecer,', nome, '!')

#nome = input('Digite seu nome: ')
#print('É um prazer te conhecer, ' + nome + '!')

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))
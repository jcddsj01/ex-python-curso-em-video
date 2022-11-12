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
print('| {} EX-027 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

nome_completo = input('Digite seu nome completo: ').strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome_completo.split(' ')[0]))
print('Seu último nome é {}'.format(nome_completo.split(' ')[-1]))

'''nome_completo = str(input('Digite seu nome completo: ')).strip()
nome_completo_format = nome_completo.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome_completo_format[0]))
print('Seu último nome é {}'.format(nome_completo_format[len(nome_completo_format)-1]))'''
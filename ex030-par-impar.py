cores_texto = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;7;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'azulclaro': '\033[1;36m',
    'cinza': '\033[1;37m'
}

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
print('| {} EX-030 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

numero = int(input('{}Me diga um número qualquer:{} '.format(cores_texto['roxo'], cores_texto['limpa'])))
if numero % 2 == 0:
    print('{}O número {} é{} {}PAR{}'.format(cores_texto['cinza'], numero, cores_texto['limpa'], cores_texto['azul'], cores_texto['limpa']))
else:
    print('{}O número {} é{} {}ÍMPAR{}'.format(cores_texto['cinza'], numero, cores_texto['limpa'], cores_texto['azul'], cores_texto['limpa']))

# ---------------------------------------------

'''
numero = int(input('{}Me diga um número qualquer:{} '.format(cores_texto['roxo'], cores_texto['limpa'])))
resultado = numero % 2
if resultado == 0:
    print('{}O número {} é{} {}PAR{}'.format(cores_texto['cinza'], numero, cores_texto['limpa'], cores_texto['azul'], cores_texto['limpa']))
else:
    print('{}O número {} é{} {}ÍMPAR{}'.format(cores_texto['cinza'], numero, cores_texto['limpa'], cores_texto['azul'], cores_texto['limpa']))
'''
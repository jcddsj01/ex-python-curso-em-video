cores_texto = {
    'limpa': '\033[m',
    'azul': '\033[1;34m',
    'cinza': '\033[1;37m',
    'roxo': '\033[1;35m'
}

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' PAR OU ÍMPAR '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

numero = int(input('{}Me diga um número qualquer:{} '.format(cores_texto['roxo'], cores_texto['limpa'])))
if numero % 2 == 0:
    print('{}O número {} é{} {}PAR{}'.format(cores_texto['cinza'], numero, cores_texto['limpa'], cores_texto['azul'], cores_texto['limpa']))
else:
    print('{}O número {} é{} {}ÍMPAR{}'.format(cores_texto['cinza'], numero, cores_texto['limpa'], cores_texto['azul'], cores_texto['limpa']))

'''
numero = int(input('{}Me diga um número qualquer:{} '.format(cores_texto['roxo'], cores_texto['limpa'])))
resultado = numero % 2
if resultado == 0:
    print('{}O número {} é{} {}PAR{}'.format(cores_texto['cinza'], numero, cores_texto['limpa'], cores_texto['azul'], cores_texto['limpa']))
else:
    print('{}O número {} é{} {}ÍMPAR{}'.format(cores_texto['cinza'], numero, cores_texto['limpa'], cores_texto['azul'], cores_texto['limpa']))
'''

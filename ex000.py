cores_texto = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;7;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'azul_claro': '\033[1;36m',
    'cinza': '\033[1;37m'
}

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m',
    'vermelho': '\033[1;41m',
    'verde': '\033[1;42m',
    'amarelo': '\033[1;43m',
    'azul': '\033[1;44m',
    'roxo': '\033[1;45m',
    'azul_claro': '\033[1;46m',
    'cinza': '\033[1;47m'
}

print('{} CORES DE TEXTO {}'.format(cores_texto['preto_branco'], cores_texto['limpa']))
print('{} CORES DE TEXTO {}'.format(cores_texto['vermelho'], cores_texto['limpa']))
print('{} CORES DE TEXTO {}'.format(cores_texto['verde'], cores_texto['limpa']))
print('{} CORES DE TEXTO {}'.format(cores_texto['amarelo'], cores_texto['limpa']))
print('{} CORES DE TEXTO {}'.format(cores_texto['azul'], cores_texto['limpa']))
print('{} CORES DE TEXTO {}'.format(cores_texto['roxo'], cores_texto['limpa']))
print('{} CORES DE TEXTO {}'.format(cores_texto['azul_claro'], cores_texto['limpa']))
print('{} CORES DE TEXTO {}\n'.format(cores_texto['cinza'], cores_texto['limpa']))

print('{} CORES DE FUNDO {}'.format(cores_fundo['preto_branco'], cores_fundo['limpa']))
print('{} CORES DE FUNDO {}'.format(cores_fundo['vermelho'], cores_fundo['limpa']))
print('{} CORES DE FUNDO {}'.format(cores_fundo['verde'], cores_fundo['limpa']))
print('{} CORES DE FUNDO {}'.format(cores_fundo['amarelo'], cores_fundo['limpa']))
print('{} CORES DE FUNDO {}'.format(cores_fundo['azul'], cores_fundo['limpa']))
print('{} CORES DE FUNDO {}'.format(cores_fundo['roxo'], cores_fundo['limpa']))
print('{} CORES DE FUNDO {}'.format(cores_fundo['azul_claro'], cores_fundo['limpa']))
print('{} CORES DE FUNDO {}\n'.format(cores_fundo['cinza'], cores_fundo['limpa']))

cabecalho = ' DEIXANDO TUDO PRONTO '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+')

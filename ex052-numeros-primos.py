cores_texto = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;7;30m',
    'vermelho': '\033[1;31m',
    'amarelo': '\033[1;33m',
    'verde': '\033[1;32m'
}

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-052 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

numero = int(input('Digite um número: '))
total = 0
for count in range(1, numero + 1):
    if numero % count == 0:
        print('{}{}{}'.format(cores_texto['amarelo'], count, cores_texto['limpa']), end=' ')
        total += 1
    else:
        print('{}{}{}'.format(cores_texto['vermelho'], count, cores_texto['limpa']), end=' ')

print('\nO número {} foi divisível {}{}{} vezes.'.format(numero, cores_texto['amarelo'], total, cores_texto['limpa']))

if total == 2:
    print('E por isso ele {}É PRIMO!{}'.format(cores_texto['verde'], cores_texto['limpa']))
else:
    print('E por isso ele {}NÃO É PRIMO!{}'.format(cores_texto['vermelho'], cores_texto['limpa']))
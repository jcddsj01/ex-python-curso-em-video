cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-038 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')

primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))

if primeiro_numero > segundo_numero:
    print('O PRIMEIRO valor é maior')
elif segundo_numero > primeiro_numero:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
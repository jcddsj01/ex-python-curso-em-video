cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-051 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

titulo2 = '   10 TERMOS DE UMA PA   '
print('=' * len(titulo2))
print(titulo2)
print('=' * len(titulo2))

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for count in range(primeiro, decimo + razao, razao):
    print('{}'.format(count), end=' -> ')
print('Acabou')
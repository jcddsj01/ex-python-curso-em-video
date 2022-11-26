cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-061 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

subtitulo = '   10 TERMOS DE UMA PA - v2.0   '
print('=' * len(subtitulo))
print(subtitulo)
print('=' * len(subtitulo))

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
count = 1
while count <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    count += 1
print('FIM')

# ------------------------------------------------

'''primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
count = 1
while count <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
    count += 1
print('FIM')'''
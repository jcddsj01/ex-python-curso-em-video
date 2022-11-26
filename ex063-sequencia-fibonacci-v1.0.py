cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-063 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

subtitulo = 'Sequência de Fibonacci '
print('_' * len(subtitulo))
print('{}'.format(subtitulo))
print('_' * len(subtitulo))

termos = int(input('Quantos termos você quer mostrar? '))
print('~' * (30))

t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
for count in range(3, termos + 1):
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
print('FIM')
print('~' * (30))

# -----------------------------------------------------------------

'''t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
count = 3
while count <= termos:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print(' -> FIM')
print('~' * (30))'''
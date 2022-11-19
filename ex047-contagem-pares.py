cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-047 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

'''for count in range(2, 50 + 1, 2):
    print(count, end=' ')
print('Acabou')'''

# ----------------------------

count = 2
while count <= 50:
    print(count, end=' ')
    count += 2
print('Acabou')
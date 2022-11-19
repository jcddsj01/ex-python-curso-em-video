cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-049 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

tabuada = int(input('Digite um número para ver sua tabuada: '))
for count in range(1, 10 + 1):
    print('{} X {:2} = {}'.format(tabuada, count, tabuada * count))

# -----------------------------

'''tabuada = int(input('Digite um número para ver sua tabuada: '))
count = 1
while count <= 10:
  print('{} x {:2} = {}'.format(tabuada, count, tabuada * count))
  count += 1'''

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-086 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for linha in range(0, 2+1):
    for coluna in range(0, 2+1):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(0, 2+1):
    for coluna in range(0, 2+1):
        print(f'[{matriz[linha][coluna]:^6}]', end='')
    print()
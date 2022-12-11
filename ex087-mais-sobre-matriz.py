cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-087 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
soma_pares = 0
soma_terceira_col = 0
maior_segunda_linha = 0
for linha in range(0, 2+1):
    for coluna in range(0, 2+1):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
for linha in range(0, 2+1):
    for coluna in range(0, 2+1):
        print(f'[{matriz[linha][coluna]:^6}] ', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print('')
print('-=' * 30)
print(f'A soma dos valores PARES é {soma_pares}.')
for linha in range(0, 3):
    soma_terceira_col += matriz[linha][2]
print(f'A soma dos valores da TERCEIRA COLUNA é {soma_terceira_col}.')
for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > maior_segunda_linha:
        maior_segunda_linha = matriz[1][coluna]
print(f'O maior valor da SEGUNDA LINHA é {maior_segunda_linha}.')
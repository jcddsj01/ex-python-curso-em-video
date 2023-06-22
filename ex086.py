cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' MATRIZ EM PYTHON '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

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

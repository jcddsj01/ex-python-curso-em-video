cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CONTAGEM DE PARES '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

'''for count in range(2, 50 + 1, 2):
    print(count, end=' ')
print('Acabou')'''

count = 2
while count <= 50:
    print(count, end=' ')
    count += 2
print('Acabou!')

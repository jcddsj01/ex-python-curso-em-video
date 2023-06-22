cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' SOMA ÍMPARES MÚLTIPLOS DE TRÊS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

soma = 0
contador = 0
for cont in range(1, 500 + 1, 2):
    if cont % 3 == 0:
        contador += 1
        soma += cont
print('A soma de todos os {} valores solicitados é {}.'.format(contador, soma))

'''cont = 1
contador = 0
soma = 0
while cont <= 500:
    if cont % 2 == 1 and cont % 3 == 0:
        contador += 1
        soma += cont
    cont += 1
print('A soma de todos os {} valores solicitados é {}.'.format(contador, soma))'''

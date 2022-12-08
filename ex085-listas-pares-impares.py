cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-085 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

numeros = [[], []]
numero = 0
for count in range(1, 7+1):
    numero = int(input(f'Digite o {count}º valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
print(f'Os valores PARES digitados foram: {numeros[0]}')
print(f'Os valores ÍMPARES digitados foram: {numeros[1]}')

# ----------------------------------------

'''numeros = list()
pares = list()
impares = list()
numero = 0
for count in range(1, 7+1):
    numero = int(input(f'Digite o {count}º valor: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
numeros.append(pares)
numeros.append(impares)
print('-=' * 30)
print(f'Os valores PARES digitados foram: {sorted(pares)}')
print(f'Os valores ÍMPARES digitados foram: {sorted(impares)}')'''
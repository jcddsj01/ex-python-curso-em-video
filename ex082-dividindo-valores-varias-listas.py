cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-082 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resposta in 'Nn':
        break
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print('-=' * 30)
print(f'A lista COMPLETA é: {numeros}')
print(f'A lista de PARES é: {pares}')
print(f'A lista de ÍMPARES é: {impares}')

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' DIVIDINDO VALORES EM VÁRIAS LISTAS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

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
print(f'A lista de PARES é: {sorted(pares)}')
print(f'A lista de ÍMPARES é: {sorted(impares)}')

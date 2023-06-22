cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' MAIOR E MENOR VALORES NA LISTA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

numeros = []
maior = 0
menor = 0
for cont in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição {cont+1}: ')))
    if cont == 0:
        maior = numeros[cont]
        menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]
print('=-' * 25)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, valor in enumerate(numeros, start=1):
    if valor == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, valor in enumerate(numeros, start=1):
    if valor == menor:
        print(f'{i}... ', end='')
print()

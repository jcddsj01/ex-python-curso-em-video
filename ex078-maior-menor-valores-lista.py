cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-078 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

numeros = []
maior = 0
menor = 0
for count in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição {count}: ')))
    if count == 0:
        maior = numeros[count]
        menor = numeros[count]
    else:
        if numeros[count] > maior:
            maior = numeros[count]
        if numeros[count] < menor:
            menor = numeros[count]
print('=-' * 25)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, valor in enumerate(numeros):
    if valor == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, valor in enumerate(numeros):
    if valor == menor:
        print(f'{i}... ', end='')
print()

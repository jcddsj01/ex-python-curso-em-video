cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-084 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

temporario = []
principal = []
maior_peso = 0
menor_peso = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior_peso = temporario[1]
        menor_peso = temporario[1]
    else:
        if temporario[1] > maior_peso:
            maior_peso = temporario[1]
        if temporario[1] < menor_peso:
            menor_peso = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi {maior_peso}Kg. Peso de ', end='')
for peso in principal:
    if peso[1] == maior_peso:
        print(f'[{peso[0]}] ', end='')
print()
print(f'O menor peso foi {menor_peso}Kg. Peso de ', end='')
for peso in principal:
    if peso[1] == menor_peso:
        print(f'[{peso[0]}] ', end='')
print()

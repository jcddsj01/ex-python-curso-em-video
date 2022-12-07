cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-080 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

numeros = list()

for count in range(0, 5):
    numero = int(input('Digite um valor: '))
    if count == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(numeros):
            if numero <= numeros[posicao]:
                numeros.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {numeros}')

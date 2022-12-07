cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-079 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

numeros = list()
while True:
    numero = int(input('Digite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(numeros)}')

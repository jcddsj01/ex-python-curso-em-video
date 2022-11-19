cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-050 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

soma = 0
contador = 0
for count in range(1, 6 + 1):
    numero = int(input('Digite o {}° valor: '.format(count)))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('Você informou {} números PARES e a soma foi {}.'.format(contador, soma))

# --------------------------------

'''soma = 0
count = 1
numero = 0
contador = 0
while count <= 6:
    numero = int(input('Digite o {}° valor: '.format(count)))
    count += 1
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('Você informou {} números PARES e a soma foi {}.'.format(contador, soma))'''

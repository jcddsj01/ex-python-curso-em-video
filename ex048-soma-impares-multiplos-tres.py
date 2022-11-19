cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-048 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

soma = 0
contador = 0
for count in range(1, 500 + 1, 2):
    if count % 3 == 0:
        contador += 1
        soma += count
print('A soma de todos os {} valores solicitados é {}.'.format(contador, soma))

# -------------------------------

'''count = 1
contador = 0
soma = 0
while count <= 500:
    if count % 2 == 1 and count % 3 == 0:
        contador += 1
        soma += count
    count += 1
print('A soma de todos os {} valores solicitados é {}.'.format(contador, soma))'''
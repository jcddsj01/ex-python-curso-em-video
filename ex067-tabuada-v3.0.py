cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-067 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('_' * 35)
    if tabuada <= 0:
        break
    for count in range(1, 10 + 1):
        print(f'{tabuada} x {count} = {tabuada * count}')
    print('_' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

# --------------------------------

'''count = 0
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('_' * 35)
    if tabuada <= 0:
        break
    while count < 10:
        count += 1
        print(f'{tabuada} x {count} = {tabuada * count}')
    print('_' * 35)
    count = 0
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')'''

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-066 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

numero = 0
count = 0
soma = 0
while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    count += 1
    soma += numero
print(f'A soma dos {count} valores foi {soma}!')

# --------------------------------------------------

'''numero = 0
count = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    count += 1
    soma += numero
count -= 1
soma -= 999
print(f'A soma dos {count} valores foi {soma}!')'''

# ----------------------------------------------------

'''numero = 0
count = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    count += 1
    soma += numero
print(f'A soma dos {count - 1} valores foi {soma - 999}!')'''

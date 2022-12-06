cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-072 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

numeros = ('zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if numero <= 0 or numero <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {numeros[numero]}')
    resposta = str(input('Você quer continuar? SIM ou NÃO: ')).strip().upper()[0]
    if resposta == 'N':
        break

# ------------------------------------------------

'''numeros = ['zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte']

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero <= 0 or numero <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros[numero]}')'''

# ------------------------------------------------

'''numeros = {0: 'zero',
           1: 'um',
           2: 'dois',
           3: 'tres',
           4: 'quatro',
           5: 'cinco',
           6: 'seis',
           7: 'sete',
           8: 'oito',
           9: 'nove',
           10: 'dez',
           11: 'onze',
           12: 'doze',
           13: 'treze',
           14: 'quatorze',
           15: 'quinze',
           16: 'dezesseis',
           17: 'dezessete',
           18: 'dezoito',
           19: 'dezenove',
           20: 'vinte'}

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero <= 0 or numero <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros[numero]}')'''

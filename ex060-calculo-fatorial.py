cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

print('+', '-' * 8, '+')
print('| {} EX-060 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')
print()

numero = int(input('Digite um número para\ncalcular seu Fatorial: '))
count = numero
fatorial = 1
print('Calculando {}! = '.format(numero), end='')
for count in range(numero, 0, -1):
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    fatorial *= count
print('{}'.format(fatorial))

# ------------------------------------

'''from math import factorial

numero = int(input('Digite um número para\ncalcular seu Fatorial: '))
fatorial = factorial(numero)
print('Calculando {}! = '.format(numero), end='')
for count in range(numero, 0, -1):
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
print('{}'.format(fatorial))'''

# ------------------------------------

#from math import factorial

#numero = int(input('''Digite um número para
#calcular seu Fatorial: '''))
#fatorial = factorial(numero)
#print('Calculando {}! = '.format(numero), end='')
#for count in range(numero, 0, -1):
#    print('{}'.format(count), end='')
#    print(' x ' if count > 1 else ' = ', end='')
#print('{}'.format(fatorial))

# -------------------------------------

'''numero = int(input('Digite um número para\ncalcular seu Fatorial: '))
count = numero
fatorial = 1
print('Calculando {}! = '.format(numero), end='')
while count >= 1:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    fatorial *= count
    count -= 1
print('{}'.format(fatorial))'''
cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CÁLCULO DO FATORIAL '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

numero = int(input('Digite um número para\ncalcular seu Fatorial: '))
cont = numero
fatorial = 1
print('Calculando {}! = '.format(numero), end='')
for cont in range(numero, 0, -1):
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
print('{}'.format(fatorial))

'''from math import factorial

numero = int(input('Digite um número para\ncalcular seu Fatorial: '))
fatorial = factorial(numero)
print('Calculando {}! = '.format(numero), end='')
for cont in range(numero, 0, -1):
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
print('{}'.format(fatorial))'''

#from math import factorial

#numero = int(input('''Digite um número para
#calcular seu Fatorial: '''))
#fatorial = factorial(numero)
#print('Calculando {}! = '.format(numero), end='')
#for cont in range(numero, 0, -1):
#    print('{}'.format(cont), end='')
#    print(' x ' if cont > 1 else ' = ', end='')
#print('{}'.format(fatorial))

'''numero = int(input('Digite um número para\ncalcular seu Fatorial: '))
cont = numero
fatorial = 1
print('Calculando {}! = '.format(numero), end='')
while cont >= 1:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))'''

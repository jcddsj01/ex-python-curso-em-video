cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'vermelho': '\033[1;41m',
    'verde': '\033[1;42m',
    'amarelo': '\033[1;43m',
    'azul': '\033[1;44m',
    'roxo': '\033[1;45m',
    'azulclaro': '\033[1;46m',
    'cinza': '\033[1;47m'
}

print('+', '-' * 8, '+')
print('| {} EX-009 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

#Tabuada usando o 'while' como estrutura de repetição (loop)
numero = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
contador = 1
while contador <= 10:
  print('{} x {:2} = {}'.format(numero, contador, numero * contador))
  contador += 1
print('-' * 12)

# --------------------------

#Tabuada usando o 'for in' com o range como estrutura de repetição (loop)
#numero = int(input('Digite um número para ver sua tabuada: '))
#print('-' * 12)
#for index in range(1, 10+1):
#  print('{} x {:2} = {}'.format(numero, index, index * numero))
#print('-' * 12)

# ----------------------------

#numero = int(input('Digite um número para ver sua tabuada: '))
#print('-' * 12)
#print('{} x {:2} = {}'.format(numero, 1,numero * 1))
#print('{} x {:2} = {}'.format(numero, 2, numero * 2))
#print('{} x {:2} = {}'.format(numero, 3, numero * 3))
#print('{} x {:2} = {}'.format(numero, 4, numero * 4))
#print('{} x {:2} = {}'.format(numero, 5, numero * 5))
#print('{} x {:2} = {}'.format(numero, 6, numero * 6))
#print('{} x {:2} = {}'.format(numero, 7, numero * 7))
#print('{} x {:2} = {}'.format(numero, 8, numero * 8))
#print('{} x {:2} = {}'.format(numero, 9, numero * 9))
#print('{} x {:2} = {}'.format(numero, 10, numero * 10))
#print('-' * 12)

# ----------------------
#numero = int(input('Digite um número para ver sua tabuada: '))
#print('-' * 12)
#print(f'{numero} x  1 = {numero * 1}')
#print(f'{numero} x  2 = {numero * 2}')
#print(f'{numero} x  3 = {numero * 3}')
#print(f'{numero} x  4 = {numero * 4}')
#print(f'{numero} x  5 = {numero * 5}')
#print(f'{numero} x  6 = {numero * 6}')
#print(f'{numero} x  7 = {numero * 7}')
#print(f'{numero} x  8 = {numero * 8}')
#print(f'{numero} x  9 = {numero * 9}')
#print(f'{numero} x 10 = {numero * 10}')
#print('-' * 12)

# -----------------------

#numero = int(input('Digite um número para ver sua tabuada: '))
#print('-' * 12)
#print('{} x  1 = {}'.format(numero, numero * 1))
#print('{} x  2 = {}'.format(numero, numero * 2))
#print('{} x  3 = {}'.format(numero, numero * 3))
#print('{} x  4 = {}'.format(numero, numero * 4))
#print('{} x  5 = {}'.format(numero, numero * 5))
#print('{} x  6 = {}'.format(numero, numero * 6))
#print('{} x  7 = {}'.format(numero, numero * 7))
#print('{} x  8 = {}'.format(numero, numero * 8))
#print('{} x  9 = {}'.format(numero, numero * 9))
#print('{} x 10 = {}'.format(numero, numero * 10))
#print('-' * 12)

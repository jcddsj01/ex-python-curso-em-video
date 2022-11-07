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
print('| {} EX-006 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = pow(numero, (1/2))

print('O dobro de {} vale {}.'.format(numero, dobro))
print('O triplo de {} vale {}.'.format(numero, triplo))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(numero, raiz_quadrada))

# -------------------------------------

#numero = int(input('Digite um número: '))
#print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(numero, (numero * 2), numero, (numero * 3), numero, (numero ** (1/2))))

# -------------------------------------

#numero = int(input('Digite um número: '))
#print('O dobro de {} vale {}.'.format(numero, (numero * 2)))
#print('O triplo de {} vale {}.'.format(numero, (numero * 3)))
#print('A raiz quadrada de {} é igual a {:.2f}.'.format(numero, (numero ** (1/2))))
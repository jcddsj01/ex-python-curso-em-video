cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' DOBRO, TRIPLO, RAIZ QUADRADA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = pow(numero, (1/2))

print('O dobro de {} vale {}.'.format(numero, dobro))
print('O triplo de {} vale {}.'.format(numero, triplo))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(numero, raiz_quadrada))

#numero = int(input('Digite um número: '))
#print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(numero, (numero * 2), numero, (numero * 3), numero, (numero ** (1/2))))

#numero = int(input('Digite um número: '))
#print('O dobro de {} vale {}.'.format(numero, (numero * 2)))
#print('O triplo de {} vale {}.'.format(numero, (numero * 3)))
#print('A raiz quadrada de {} é igual a {:.2f}.'.format(numero, (numero ** (1/2))))

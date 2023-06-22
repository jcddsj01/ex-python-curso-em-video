cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' SEQUÊNCIA DE FIBONACCI V1.0 '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

titulo = 'Sequência de Fibonacci '
print('_' * len(titulo))
print('{}'.format(titulo))
print('_' * len(titulo))

termos = int(input('Quantos termos você quer mostrar? '))
print('~' * (30))

t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
for cont in range(3, termos + 1):
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
print('FIM')
print('~' * (30))

'''t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~' * (30))'''

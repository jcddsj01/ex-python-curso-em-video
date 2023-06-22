cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' LISTA DE PREÇOS COM TUPLA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
listagem = ('Lápis', 1.75,
           'Borracha', 2.00,
           'Caderno', 15.90,
           'Estojo', 25.00,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.32,
           'Canetas', 22.30,
           'Livro', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)

'''print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
listagem = (('Lápis', 1.75),
                   ('Borracha', 2.00),
                   ('Caderno', 15.90),
                   ('Estojo', 25.00),
                   ('Transferidor', 4.20),
                   ('Compasso', 9.99),
                   ('Mochila', 120.32),
                   ('Canetas', 22.30),
                   ('Livro', 34.90))
for item in listagem:
    print(item[0] + '.' * 20 + 'R$', item[1])
    print(f'{item[0]:.<30}', end='')
    print(f'R${item[1]:>7.2f}')
print('-' * 40)'''

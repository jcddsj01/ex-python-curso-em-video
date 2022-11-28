cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-070 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

total_compra = 0
produtos_maior_mil = 0
count = 0
menor_preco = 0
produto_mais_barato = ''
while True:
    print('-' * 30)
    print('     LOJA SUPER BARATÃO      ')
    print('-' * 30)
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço R$ '))
    count += 1
    total_compra += preco
    if preco > 1000:
        produtos_maior_mil += 1

    if count == 1 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^50}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total_compra:.2f}')
print(f'Temos {produtos_maior_mil} produto(s) custando mais de R$ 1.000,00')
print(f'O Produto mais barato foi {produto_mais_barato} que custa R$ {menor_preco:.2f}')

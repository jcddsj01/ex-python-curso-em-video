cores_texto = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;7;30m',
    'vermelho': '\033[1;31m',
    'amarelo': '\033[1;33m'
}

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m',
    'amarelo': '\033[1;33m'
}

cabecalho = ' GERENCIADOR DE PAGAMENTOS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

print('{}{:=^40}{}'.format(cores_fundo['amarelo'], ' LOJAS GUANABARA ', cores_fundo['limpa']))

preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''', end='')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * (10 / 100))
elif opcao == 2:
    total = preco - (preco * (5 / 100))
elif opcao == 3:
    total = preco
    parcelas = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} {}SEM JUROS{}.'.format(parcelas, cores_texto['amarelo'], cores_texto['limpa']))
elif opcao == 4:
    total = preco + (preco * (20 / 100))
    parcelas = int(input('Quantas parcelas? '))
    juros_parcela = total / parcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f} {}COM JUROS{}.'.format(parcelas, juros_parcela, cores_texto['vermelho'], cores_texto['limpa']))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))

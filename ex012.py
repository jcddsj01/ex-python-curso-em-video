cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CALCULANDO DESCONTOS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

preco = float(input('Qual é o preço do produto? R$ '))
desconto = 5
preco_desconto = preco - (preco * desconto / 100)
print('O produto que custava R$ {:.2f}, na promoção com desconto de {}% vai custar R$ {:.2f}'.format(preco, desconto, preco_desconto))

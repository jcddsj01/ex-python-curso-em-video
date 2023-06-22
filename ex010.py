cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CONVERSOR DE MOEDAS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
cotacao_dolar = float(input('Qual é a cotação do dolar? US$ '))
dolar = real / cotacao_dolar
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))

#real = float(input('Quanto dinheiro você tem na carteira? R$'))
#dolar = real / 3.27
#print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

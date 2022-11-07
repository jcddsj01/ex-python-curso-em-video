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
print('| {} EX-010 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

real = float(input('Quanto dinheiro você tem na carteira? R$'))
cotacao_dolar = float(input('Qual é a cotação do dolar? US$'))
dolar = real / cotacao_dolar
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

# -----------------------------

#real = float(input('Quanto dinheiro você tem na carteira? R$'))
#dolar = real / 3.27
#print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
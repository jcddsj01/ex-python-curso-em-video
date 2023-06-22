cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' ALUGUEL DE CARROS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

dias_alugados = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))
total_pagar = (dias_alugados * 60) + (km_rodados * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(total_pagar))

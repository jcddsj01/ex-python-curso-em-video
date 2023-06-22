cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' APROVANDO EMPRÉSTIMO '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
financiamento = int(input('Quantos anos de financiamento? '))
prestacao = valor_casa / (financiamento * 12)
minimo = salario * (30 / 100)

print('Para pagar um casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f} reais.'.format(valor_casa, financiamento, prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

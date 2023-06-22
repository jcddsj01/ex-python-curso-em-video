import moeda

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' FORMATANDO MOEDAS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

p = float(input(f'Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
t = int(input('\nQual o valor da taxa: '))
print(f'Aumentando {t}%, temos {moeda.aumentar(p, t, True)}')
print(f'Reduzindo {t}%, temos {moeda.diminuir(p, t, True)}')

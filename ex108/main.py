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
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
t = int(input('\nQual o valor da taxa: '))
print(f'Aumentando {t}%, temos {moeda.moeda(moeda.aumentar(p, t))}')
print(f'Reduzindo {t}%, temos {moeda.moeda(moeda.diminuir(p, t))}')

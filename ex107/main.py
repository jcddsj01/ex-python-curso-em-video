import moeda

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' EXERCITANDO MÓDULOS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p:.2f} é R$ {moeda.metade(p):.2f}')
print(f'O dobro de R$ {p:.2f} é R$ {moeda.dobro(p):.2f}')
t = int(input('\nQual o valor da taxa: '))
print(f'Aumentando {t}%, temos R$ {moeda.aumentar(p, t):.2f}')
print(f'Reduzindo {t}%, temos R$ {moeda.diminuir(p, t):.2f}')

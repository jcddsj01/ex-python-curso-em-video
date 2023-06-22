from ex111.utilidadescev import moeda

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' TRANSFORMANDO MÓDULOS EM PACOTES '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

p = float(input('Digite o preço: R$ '))
ta = int(input('Qual o valor da taxa de aumento: '))
tr = int(input('Qual o valor da taxa de redução: '))
moeda.resumo(p, ta, tr)

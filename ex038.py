cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' COMPARANDO NÚMEROS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))

if primeiro_numero > segundo_numero:
    print('O PRIMEIRO valor é maior')
elif segundo_numero > primeiro_numero:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')

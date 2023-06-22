cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' PROGRESSÃO ARITMÉTICA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

titulo = '   10 TERMOS DE UMA PA   '
print('=' * len(titulo))
print(titulo)
print('=' * len(titulo))

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for cont in range(primeiro, decimo + razao, razao):
    print('{}'.format(cont), end=' -> ')
print('Acabou!')

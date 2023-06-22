cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' VALIDAÇÃO DE DADOS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while True:
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
    else:
        print('Sexo {} registrado com sucesso.'.format(sexo))
        break'''

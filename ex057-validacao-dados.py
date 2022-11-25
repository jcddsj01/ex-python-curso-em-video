cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-057 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

# --------------------------------

'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while True:
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
    else:
        print('Sexo {} registrado com sucesso.'.format(sexo))
        break'''
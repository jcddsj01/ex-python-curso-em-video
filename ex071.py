cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cores_texto = {
    'limpa': '\033[m',
    'vermelho': '\033[1;31m'
}

cabecalho = ' SIMULADOR DE CAIXA ELETÔNICO '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

print('=' * 30)
print('{}{:^30}{}'.format(cores_texto['vermelho'], 'BANCO CEV', cores_texto['limpa']))
print('=' * 30)

valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
cedula = 100
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédula(s) de R$ {cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

'''valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédula(s) de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''

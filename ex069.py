cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' ANÁLISE DE DADOS DO GRUPO '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')


maior18 = 0
total_homens = 0
total_mulheres_menor20 = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA   ')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres_menor20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {total_homens} homem(s) cadastrado(s).')
print(f'E temos {total_mulheres_menor20} mulher(es) com menos de 20 anos.')

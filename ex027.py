cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

nome_completo = input('Digite seu nome completo: ').strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome_completo.split(' ')[0]))
print('Seu último nome é {}'.format(nome_completo.split(' ')[-1]))

'''nome_completo = str(input('Digite seu nome completo: ')).strip()
nome_completo_format = nome_completo.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome_completo_format[0]))
print('Seu último nome é {}'.format(nome_completo_format[len(nome_completo_format)-1]))'''

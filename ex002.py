cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' RESPONDENDO AO USUÁRIO '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

#nome = input('Digite seu nome: ')
#print('É um prazer te conhecer,', nome, '!')

#nome = input('Digite seu nome: ')
#print('É um prazer te conhecer, ' + nome + '!')

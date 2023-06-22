cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' PROCURANDO UMA STRING DENTRO DE OUTRA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

nome = str(input('Qual é seu nome completo? ')).strip()

# O operador 'in' verifica se o operando a sua esquerda,
# está contido na lista a sua direita, da mesma forma que
# o operador not in que verifica o contrário.
print('Seu nome tem Silva? {}'.format('silva' in nome.capitalize()))

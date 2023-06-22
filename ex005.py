cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' ANTECESSOR E SUCESSOR '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

num = int(input('Digite um número: '))

# a = num - 1
# s = num + 1

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(num, (num-1), (num+1)))

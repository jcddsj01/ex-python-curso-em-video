cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' TRATANDO VÁRIOS VALORES V1.0 '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

numero = 0
cont = 0
soma = 0
numero = int(input('Digite um número OU [999 para parar]: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número OU [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

# numero = 0
# cont = 0
# soma = 0
# while numero != 999:
#     numero = int(input('Digite um número OU [999 para parar]: '))
#     soma += numero
#     cont += 1
# print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, soma - 999))

# numero = 0
# cont = 0
# soma = 0
# while True:
#     numero = int(input('Digite um número OU [999 para parar]: '))
#     if numero == 999:
#         break
#     cont += 1
#     soma += numero
# print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

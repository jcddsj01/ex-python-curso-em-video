cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' VÁRIOS NÚMEROS COM FLAG '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

numero = 0
cont = 0
soma = 0
while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'A soma dos {cont} valores foi {soma}!')

'''numero = 0
cont = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += numero
cont -= 1
soma -= 999
print(f'A soma dos {cont} valores foi {soma}!')'''

'''numero = 0
cont = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += numero
print(f'A soma dos {cont - 1} valores foi {soma - 999}!')'''

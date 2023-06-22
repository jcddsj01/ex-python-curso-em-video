cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' SOMA DOS PARES '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

soma = 0
contador = 0
for count in range(1, 6 + 1):
    numero = int(input('Digite o {}° valor: '.format(count)))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('Você informou {} números PARES e a soma foi {}.'.format(contador, soma))

'''soma = 0
cont = 1
numero = 0
contador = 0
while cont <= 6:
    numero = int(input('Digite o {}° valor: '.format(cont)))
    cont += 1
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('Você informou {} números PARES e a soma foi {}.'.format(contador, soma))'''

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' TABUADA V2.0 '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

tabuada = int(input('Digite um número para ver sua tabuada: '))
for cont in range(1, 10 + 1):
    print('{} X {:2} = {}'.format(tabuada, cont, tabuada * cont))

'''tabuada = int(input('Digite um número para ver sua tabuada: '))
cont = 1
while cont <= 10:
  print('{} x {:2} = {}'.format(tabuada, cont, tabuada * cont))
  cont += 1'''

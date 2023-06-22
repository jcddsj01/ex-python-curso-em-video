cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' TABUADA V3.0 '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print()
    print('_' * 35)
    if tabuada <= 0:
        break
    for cont in range(1, 10 + 1):
        print(f'{tabuada} x {cont} = {tabuada * cont}')
    print('_' * 35)
    print()
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

# cont = 0
# while True:
#     tabuada = int(input('Quer ver a tabuada de qual valor? '))
#     print()
#     print('_' * 35)
#     if tabuada <= 0:
#         break
#     while cont < 10:
#         cont += 1
#         print(f'{tabuada} x {cont} = {tabuada * cont}')
#     print('_' * 35)
#     print()
#     cont = 0
# print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

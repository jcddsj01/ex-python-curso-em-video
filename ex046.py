from time import sleep

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CONTAGEM REGRESSIVA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

for count in range(10, 0, -1):
    print(count)
    sleep(1)
print('BUM! BUM! POOOW!')

'''count = 10
while count >= 1:
    print(count)
    sleep(1)
    count -= 1
print('BUM! BUM! POOOW!')'''

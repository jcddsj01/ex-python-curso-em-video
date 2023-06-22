from time import sleep

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' FUNÇÃO DE CONTADOR '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

def contador(i, f, p):
    print('-=' * 15)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)
    p = abs(p)
    if p == 0:
        p = 1
        print(f'{i}', end=' ', flush=True)
    if f < i:
        p *= -1
        f -= 2
    for i in range(i, f + 1, p):
        print(f'{i}', end=' ', flush=True)
        i -= p
        sleep(0.5)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 15)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)

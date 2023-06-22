from time import sleep

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' FUNÇÃO QUE DESCOBRE O MAIOR '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

def maior(*numeros):
    print('-=' * 25)
    print('Analisando os valores passados...')
    cont = maior = 0
    for numero in numeros:
        print(numero, end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
        cont += 1
    if len(numeros) > 1:
        print(f'Foram informados {cont} valores ao todo.')
        print(f'O maior valor informado foi {maior}.')
    elif len(numeros) == 1:
        print(f'Foi informado {cont} valor ao todo.')
        print(f'O maior valor informado foi {maior}.')
    else:
        print(f'Nenhum valor foi informado.')
        print(f'Não foi informado o maior valor.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

from time import sleep

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' FUNÇÃO QUE DESCOBRE O MAIOR ', Cores.PRETO_BRANCO)

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
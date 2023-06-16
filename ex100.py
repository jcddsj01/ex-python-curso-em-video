from random import randint
from time import sleep

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' FUNÇÃO PARA SORTEAR E SOMAR ', Cores.PRETO_BRANCO)

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        valor = randint(1, 10)
        lista.append(valor)
        print(f'{valor} ', end='', flush=True)
        sleep(0.8)
    print('PRONTO!')

def somaPar(lista):
    soma_par = 0
    for num in lista:
        if num % 2 == 0:
           soma_par += num
    print(f'Somando os valores pares de {lista}, temos {soma_par}')

numeros = list()
sorteia(numeros)
somaPar(numeros)
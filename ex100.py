from random import randint
from time import sleep

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' FUNÇÕES PARA SORTEAR E SOMAR '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

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

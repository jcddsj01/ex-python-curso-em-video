from random import randint
from time import sleep
from operator import itemgetter

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' JOGO DE DADOS EM PYTHON ', Cores.PRETO_BRANCO)

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}

classificacao = list()

print('Valores sorteados:')

for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)

classificacao = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 25)

print('  == CLASSIFICAÇÃO DOS JOGADORES == ')

for indice, valor in enumerate(classificacao):
    print(f'    {indice+1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(1)

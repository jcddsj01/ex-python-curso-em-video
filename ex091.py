from random import randint
from time import sleep
from operator import itemgetter

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' JOGO DE DADOS EM PYTHON '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

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

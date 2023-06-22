from random import choice
from time import sleep

cores_texto = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;7;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m'
}

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' JOGO DA ADIVINHAÇÃO V1.0 '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

print('{}-=-{}'.format(cores_texto['amarelo'], cores_texto['limpa']) * 20)
print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...{}'.format(cores_texto['azul'], cores_texto['limpa']))
print('{}-=-{}'.format(cores_texto['amarelo'], cores_texto['limpa']) * 20)
numero_computador = choice(range(0, 5 + 1))
numero_jogador = int(input('\nEm que número eu pensei? '))
print()
print('{}PROCESSANDO...{}'.format(cores_texto['roxo'], cores_texto['limpa']))
sleep(2)
if numero_computador != numero_jogador:
    print('{}GANHEI! Eu pensei no número {} e não no {}{}!'.format(cores_texto['vermelho'], numero_computador, numero_jogador, cores_texto['limpa']))
else:
    print('{}PARABÉNS! Você conseguiu me vencer!{}'.format(cores_texto['verde'], cores_texto['limpa']))

cores_texto = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;7;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'azulclaro': '\033[1;36m',
    'cinza': '\033[1;37m'
}

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'vermelho': '\033[1;41m',
    'verde': '\033[1;42m',
    'amarelo': '\033[1;43m',
    'azul': '\033[1;44m',
    'roxo': '\033[1;45m',
    'azulclaro': '\033[1;46m',
    'cinza': '\033[1;47m'
}

print('+', '-' * 8, '+')
print('| {} EX-028 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')
print()

print('{}-=-{}'.format(cores_texto['amarelo'], cores_texto['limpa']) * 20)
print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...{}'.format(cores_texto['azul'], cores_texto['limpa']))
print('{}-=-{}'.format(cores_texto['amarelo'], cores_texto['limpa']) * 20)

from random import choice
#from random import randint
from time import sleep

#numero_computador = randint(0, 5)

numero_computador = choice(range(0, 5 + 1))
numero_jogador = int(input('Em que número eu pensei? '))
print()

print('{}PROCESSANDO...{}'.format(cores_texto['roxo'], cores_texto['limpa']))
sleep(2)

if numero_computador != numero_jogador:
    print('{}GANHEI! Eu pensei no número {} e não no {}{}!'.format(cores_texto['vermelho'], numero_computador, numero_jogador, cores_texto['limpa']))
else:
    print('{}PARABÉNS! Você conseguiu me vencer!{}'.format(cores_texto['verde'], cores_texto['limpa']))
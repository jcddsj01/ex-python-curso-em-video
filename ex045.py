from random import randint
from time import sleep

cores_texto = {
    'limpa': '\033[m',
    'azul_claro': '\033[1;36m'
}

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' GAME: PEDRA - PAPEL - TESOURA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

print(f"{cores_texto['azul_claro']}{' JOKENPÔ ':=^40}{cores_texto['limpa']}")

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''', end='')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

'''from random import choice
from time import sleep

print('''#Suas opções:
#[ 0 ] PEDRA
#[ 1 ] PAPEL
#[ 2 ] TESOURA
''', end='')

jogador = int(input('Qual é a sua jogada? '))
computador = choice(range(0, 2 + 1))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)

if computador == 0:
    print('Computador jogou Pedra')
elif computador == 1:
    print('Computador jogou Papel')
elif computador == 2:
    print('Computador jogou Tesoura')

if jogador == 0:
    print('Jogador jogou Pedra')
elif jogador == 1:
    print('Jogador jogou Papel')
elif jogador == 2:
    print('Jogador jogou Tesoura')

print('-=' * 12)
if jogador == computador:
    print('EMPATE')
elif jogador == 0 and computador == 1:
    print('COMPUTADOR VENCE')
elif jogador == 1 and computador == 0:
    print('JOGADOR VENCE')
elif jogador == 0 and computador == 2:
    print('JOGADOR VENCE')
elif jogador == 2 and computador == 0:
    print('COMPUTADOR VENCE')
elif jogador == 2 and computador == 1:
    print('JOGADOR VENCE')
elif jogador == 1 and computador == 2:
    print('COMPUTADOR VENCE')'''

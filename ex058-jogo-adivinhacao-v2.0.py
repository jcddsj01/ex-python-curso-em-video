cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

print('+', '-' * 8, '+')
print('| {} EX-058 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')
print()

from random import randint
computador = randint(0, 10)


print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativa(s). Parabéns!'.format(palpites))

# -----------------------------------

'''from random import choice
computador = choice(range(0, 10 + 1))

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativa(s). Parabéns!'.format(palpites))'''

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-088 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

print('-' * 30)
print('      JOGA NA MEGA SENA    ')
print('-' * 30)

from random import sample
from time import sleep

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {quantidade} JOGOS', '-=' * 3)
count = 1
jogos = []
while count <= quantidade:
    jogos.append(sample(range(1, 61), 6))
    count += 1
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}: {sorted(lista)}')
    sleep(1)
print('-=' * 4, '< BOA SORTE! >', '-=' * 4)
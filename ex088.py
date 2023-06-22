from random import sample
from time import sleep

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' PALPITES PARA A MEGA SENA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

print('-' * 30)
print('      JOGA NA MEGA SENA    ')
print('-' * 30)

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {quantidade} JOGO(S)', '-=' * 3)
cont = 1
jogos = []
while cont <= quantidade:
    jogos.append(sample(range(1, 61), 6))
    cont += 1
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}: {sorted(lista)}')
    sleep(1)
print('-=' * 4, '< BOA SORTE! >', '-=' * 4)

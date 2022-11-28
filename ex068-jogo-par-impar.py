cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-068 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

nome_jogo = 'VAMOS JOGAR PAR OU IMPAR'
print('=' * len(nome_jogo))
print(f'{nome_jogo}')
print('=' * len(nome_jogo))

from random import randint

vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('PAR ou IMPAR? [P/I]: ')).strip().upper()[0]
    print('_' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print('_' * 30)
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('=-' * 15)
print(f'GAME OVER! Você venceu {vitoria} vezes.')


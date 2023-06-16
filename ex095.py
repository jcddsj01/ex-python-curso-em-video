class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'

def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}')

cabecalho(' APRIMORANDO OS DICIONÁRIOS ', Cores.PRETO_BRANCO)

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = input('\nNome do Jogador: ').capitalize()
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for count in range(0, total):
        partidas.append(int(input(f'  Quantos gols na partida {count + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = input('\nQuer continuar? [S/N]: ').upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break

print()
print('-=' * 40)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i.capitalize():<15}', end='')
print()
print('-' * 40)
for c, v in enumerate(time):
    print(f'{c:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)

while True:
    busca = int(input('\nMostrar dados de qual jogador? (999 - Finaliza): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'\n-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gol(s).')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

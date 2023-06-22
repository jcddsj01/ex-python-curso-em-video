cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' APRIMORANDO OS DICIONÁRIOS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+')

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = input('\nNome do Jogador: ').capitalize()
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for cont in range(0, total):
        partidas.append(int(input(f'  Quantos gols na partida {cont + 1}? ')))
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
        jogador = time[busca]
        print(f'\n-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(jogador['gols']):
            print(f'    No jogo {i + 1} fez {g} gol(s).')
        if not jogador['gols']:
            print('     Nenhum gol foi marcado.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

'''time = []
while True:
    jogador = {}
    partidas = []
    jogador['nome'] = input('\nNome do Jogador: ').capitalize()
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for cont in range(1, total + 1):
        partidas.append(int(input(f'Quantos gols na partida {cont}? ')))
    jogador['gols'] = partidas
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = input('\nQuer continuar? [S/N]: ').upper()
        if resposta in ['S', 'N']:
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break

print()
print('-=' * 40)
print(f'{"Cod":<5}{"Nome":<15}{"Gols":<20}{"Total":<10}')
print('-' * 55)
for c, jogador in enumerate(time):
    cod = str(c)
    nome = jogador['nome']
    gols = str(jogador['gols'])
    total = str(jogador['total'])
    print(f'{cod:<5}{nome:<15}{gols:<20}{total:<10}')
print('-=' * 40)

while True:
    busca = int(input('\nMostrar dados de qual jogador? (999 - Finaliza): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        jogador = time[busca]
        print(f'\n-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
        for i, g in enumerate(jogador['gols']):
            partida = i + 1
            print(f'    No jogo {partida} fez {g} gol(s).')
        if not jogador['gols']:
            print('    Nenhum gol foi marcado.')
    print('-' * 40)

print('<< VOLTE SEMPRE >>')'''

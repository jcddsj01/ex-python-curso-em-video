class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' CADASTRO DE JOGADOR DE FUTEBOL ', Cores.PRETO_BRANCO)

jogador = dict()
partidas = list()

jogador['nome'] = input('Nome do Jogador: ').capitalize()
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for count in range(0, total):
    partidas.append(int(input(f'  Quantos gols na partida {count+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partida(s).')
for indice, gols in enumerate(jogador['gols']):
    print(f'    => Na partida {indice+1}, fez {gols} gol(s).')
print(f'Foi um total de {jogador["total"]} gol(s).')

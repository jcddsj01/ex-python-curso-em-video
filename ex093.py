cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CADASTRO DE JOGADOR DE FUTEBOL '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

jogador = dict()
partidas = list()
jogador['nome'] = input('Nome do Jogador: ').capitalize()
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for cont in range(0, total):
    partidas.append(int(input(f'  Quantos gols na partida {cont+1}? ')))
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

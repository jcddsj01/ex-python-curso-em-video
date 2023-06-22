cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' FICHA DO JOGADOR '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador(a) {jogador} fez {gol} gol(s) no campeonato.')

print('-' * 30)
nome = input('Nome do Jogador(a): ').capitalize()
gols = str(input('Número de Gol(s): '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)

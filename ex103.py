class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'

def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')

cabecalho(' FICHA DO JOGADOR ', Cores.PRETO_BRANCO)
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

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' UM PRINT ESPECIAL ', Cores.PRETO_BRANCO)

def escreva(msg):
    t = len(msg) + 4
    print('~' * t)
    print(f'  {msg}')
    print('~' * t)

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')

# -----------------------------------------------

'''def escreva(msg):
    t = len(msg) + 4
    print('~' * t)
    print(f'  {msg}')
    print('~' * t)

m = input('Digite um texto: ')
escreva(m)'''
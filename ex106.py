from time import sleep

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' SISTEMA INTERATIVO DE AJUDA ', Cores.PRETO_BRANCO)

def painel():
    painel = '| SISTEMA DE AJUDA PyHELP |'
    print(f"{Cores.PRETO_BRANCO}{'~' * len(painel)}{Cores.SEM_COR}")
    print(f"{Cores.PRETO_BRANCO}{painel}{Cores.SEM_COR}")
    print(f"{Cores.PRETO_BRANCO}{'~' * len(painel)}{Cores.SEM_COR}")

def ajuda(comando):
    ajuda = f'  Acessando o manual do comando \'{comando}\''
    print(f"\n'~' * len(ajuda)")
    print(ajuda)
    print('~' * len(ajuda))
    print(end='')
    print('Aguarde...')
    sleep(1)
    print()
    help(comando)
    print(end='')

while True:
    print(end='')
    painel()
    comando = input("Função, Biblioteca ou 'FIM' para Sair > ")
    if comando.upper() == 'FIM':
        fim = '  ATÉ LOGO!  '
        print('Aguarde...')
        sleep(1)
        print('~' * len(fim))
        print(fim)
        print('~' * len(fim))
        break
    else:
        ajuda(comando)

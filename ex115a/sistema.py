from ex115a.lib.interface import *
from time import sleep

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho_header(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')

cabecalho_header(' CRIANDO UM MENU ', Cores.PRETO_BRANCO)

while True:
    resp = menu(['Cadastros', 'Novo cadastro', 'Sair'])
    if resp == 1:
        cabecalho('Opção 1')
    elif resp == 2:
        cabecalho('Opção 2')
    elif resp == 3:
        cabecalho('\033[1;33mSaindo do sistema... Até logo!\033[m')
        break
    else:
       print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

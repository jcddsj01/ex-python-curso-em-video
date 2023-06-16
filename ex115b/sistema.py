from ex115b.lib.interface import *
from ex115b.lib.arquivo import *
from time import sleep

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' ARQUIVOS ', Cores.PRETO_BRANCO)

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Cadastros', 'Novo cadastro', 'Sair'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastro(arq, nome, idade)
    elif resp == 3:
        cabecalho('\033[1;33mSaindo do sistema... Até logo!\033[m')
        break
    else:
       print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

from ex115a.lib.interface import *
from time import sleep

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CRIANDO UM MENU '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

while True:
    resp = menu(['Cadastros', 'Novo cadastro', 'Sair'])
    if resp == 1:
        cabecalho_secundario('Opção 1')
    elif resp == 2:
        cabecalho_secundario('Opção 2')
    elif resp == 3:
        cabecalho_secundario('Saindo do sistema... Até logo!')
        break
    else:
       print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

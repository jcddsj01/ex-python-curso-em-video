from time import sleep

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' SISTEMA INTERATIVO DE AJUDA EM PYTHON '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

def painel():
    painel = '| SISTEMA DE AJUDA PyHELP |'
    print('~' * len(painel))
    print(f"{cores_fundo['preto_branco']}{painel}{cores_fundo['limpa']}")
    print('~' * len(painel))

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

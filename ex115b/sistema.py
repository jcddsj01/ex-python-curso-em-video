from ex115b.lib.interface import *
from ex115b.lib.arquivo import *
from time import sleep

cores_texto = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;7;30m',
    'vermelho': '\033[1;31m'
}

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' DEIXANDO TUDO PRONTO '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Cadastros', 'Novo cadastro', 'Sair'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho_secundario('NOVO CADASTRO')
        nome = input('Nome: ').capitalize()
        idade = leiaInt('Idade: ')
        cadastro(arq, nome, idade)
    elif resp == 3:
        cabecalho_secundario('Saindo do sistema... Até logo!')
        break
    else:
       print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

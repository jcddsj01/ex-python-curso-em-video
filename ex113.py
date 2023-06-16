class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}')


cabecalho(' FUNÇÕES APROFUNDADAS ', Cores.PRETO_BRANCO)

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mInterrompido pelo usuário.\033[m')
            return 0
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print('\033[1;31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mInterrompido pelo usuário.\033[m')
            return 0
        else:
            return num

num_int = leiaInt('\nDigite um Inteiro: ')
num_float = leiaFloat('Digite um Real: ')
print(f'\nO valor inteiro digitado foi {num_int} e o real foi {num_float:.2f}')

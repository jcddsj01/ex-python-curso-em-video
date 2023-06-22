cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' FUNÇÕES APROFUNDADAS EM PYTHON '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

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

num_int = leiaInt('Digite um Inteiro: ')
num_float = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {num_int} e o real foi {num_float:.2f}')

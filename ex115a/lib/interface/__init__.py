def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            break
        else:
            return num

def linha(tam=42):
    return print('-'*tam)

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(list):
    cabecalho('MENU PRINCIPAL')
    count = 1
    for item in list:
        print(f'\033[33m{count}\033[m - \033[34m{item}\033[m')
        count += 1
    print('-' * 42)
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc

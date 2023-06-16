class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' FUNÇÃO PARA FATORIAL ', Cores.PRETO_BRANCO)

def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (Opcional) Mostra ou não o cálculo.
    :return: Retorna o resultado do Fatorial.
    """
    if numero < 0:
        return None

    fat = 1
    for count in range(numero, 0, -1):
        if show:
            print(count, end=' ')
            if count > 1:
                print('x ', end='')
            else:
                print('=', end=' ')
        fat *= count
    return fat

print('-' * 25)
print(fatorial(7, True))
# help(fatorial)
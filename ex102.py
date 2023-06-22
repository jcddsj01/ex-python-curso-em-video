cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' FUNÇÃO PARA FATORIAL '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

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
    for cont in range(numero, 0, -1):
        if show:
            print(cont, end=' ')
            if cont > 1:
                print('x ', end='')
            else:
                print('=', end=' ')
        fat *= cont
    return fat

print('-' * 25)
print(fatorial(7, True))
# help(fatorial)

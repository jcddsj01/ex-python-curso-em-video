import moeda

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' FORMATANDO MOEDAS ', Cores.PRETO_BRANCO)

p = float(input(f'Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
t = int(input('Qual o valor da taxa: '))
print(f'Aumentando {t}%, temos {moeda.aumentar(p, t, True)}')
print(f'Reduzindo {t}%, temos {moeda.diminuir(p, t, True)}')

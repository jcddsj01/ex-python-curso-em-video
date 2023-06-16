from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado


class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' ENTRADA DE DADOS MONETÁRIOS ', Cores.PRETO_BRANCO)

p = dado.leiaDinheiro('Digite o preço: R$ ')
ta = int(input('Qual o valor da taxa de aumento: '))
tr = int(input('Qual o valor da taxa de redução: '))
moeda.resumo(p, ta, tr)

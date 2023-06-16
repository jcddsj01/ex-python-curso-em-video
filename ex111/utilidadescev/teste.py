from ex111.utilidadescev import moeda

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' TRANSFORMANDO MÓDULOS EM PACOTES ', Cores.PRETO_BRANCO)

p = float(input('Digite o preço: R$ '))
ta = int(input('Qual o valor da taxa de aumento: '))
tr = int(input('Qual o valor da taxa de redução: '))
moeda.resumo(p, ta, tr)

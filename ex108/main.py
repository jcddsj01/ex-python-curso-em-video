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
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
t = int(input('Qual o valor da taxa: '))
print(f'Aumentando {t}%, temos {moeda.moeda(moeda.aumentar(p, t))}')
print(f'Reduzindo {t}%, temos {moeda.moeda(moeda.diminuir(p, t))}')

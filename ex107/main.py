import moeda

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' EXERCITANDO MÓDULOS ', Cores.PRETO_BRANCO)

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p:.2f} é R$ {moeda.metade(p):.2f}')
print(f'O dobro de R$ {p:.2f} é R$ {moeda.dobro(p):.2f}')
t = int(input('Qual o valor da taxa: '))
print(f'Aumentando {t}%, temos R$ {moeda.aumentar(p, t):.2f}')
print(f'Reduzindo {t}%, temos R$ {moeda.diminuir(p, t):.2f}')

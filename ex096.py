class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' FUNÇÃO QUE CALCULA ÁREA ', Cores.PRETO_BRANCO)

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um TERRENO de {largura:.2f} X {comprimento:.2f} é de {a:.2f}m².')

titulo = ' Controle de Terrenos '
print(titulo)
print('-' * len(titulo))

# Programa principal
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

# ----------------------------------------------------------------

'''def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um TERRENO de {largura:.2f} X {comprimento:.2f} é de {a:.2f}m².')

titulo = ' Controle de Terrenos '
print(titulo)
print('-' * len(titulo))

try:
    l = float(input('LARGURA (m): '))
except:
    print('Erro! Você digitou uma vírgula ao invés de um ponto.')
l = float(input('Insira novamente a LARGURA (m) ex: 0.0: '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)'''
from datetime import date

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' CADASTRO DE TRABALHADOR ', Cores.PRETO_BRANCO)

cadastro = {}
cadastro['nome'] = input('Nome: ')
ano_nasc = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
cadastro['idade'] = ano_atual - ano_nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - ano_atual)
print('-=' * 30)
for chave, valor in cadastro.items():
    print(f'  - {chave} tem o valor {valor}')

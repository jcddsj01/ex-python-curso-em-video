class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' FUNÇÃO PARA VOTAÇÃO ', Cores.PRETO_BRANCO)

def voto(ano):
    from datetime import date
    data_atual = date.today().year
    idade = data_atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

print('-' * 30)
ano_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_nascimento))

# -------------------------------------

'''def voto(ano):
    from datetime import date
    data_atual = date.today().year
    idade = data_atual - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO VOTA')
    elif 16 <= idade < 18 or idade > 65:
        print('OPCIONAL')
    else:
        print('OBRIGATÓRIO')

print('-' * 30)
ano_nascimento = int(input('Em que ano você nasceu? '))
voto(ano_nascimento)'''
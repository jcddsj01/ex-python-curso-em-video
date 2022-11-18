cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'verde': '\033[1;42m'
}

titulo = ' EX-039 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

titulo = ' ALISTAMENTO MILITAR '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['verde'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))
if idade < 18:
    print('Ainda falta(m) {} ano(s) para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}'.format(ano_atual + (18 - idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} ano(s).'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano_atual - (idade - 18)))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')

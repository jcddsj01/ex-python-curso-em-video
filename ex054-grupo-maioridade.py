cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-054 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')

from datetime import date

ano_atual = date.today().year
total_maior = 0
total_menor = 0
for count in range(1, 7 + 1):
    ano_nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(count)))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print('Ao todo tivemos {} pessoa(s) maiore(s) de idade.'.format(total_maior))
print('E também {} pessoa(s) menore(s) de idade.'.format(total_menor))
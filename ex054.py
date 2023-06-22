from datetime import date

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' GRUPO DA MAIORIDADE '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

ano_atual = date.today().year
total_maior = 0
total_menor = 0
for count in range(1, 7 + 1):
    ano_nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(count)))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print('Ao todo tivemos {} pessoa(s) maiore(s) de idade.'.format(total_maior))
print('E também {} pessoa(s) menore(s) de idade.'.format(total_menor))

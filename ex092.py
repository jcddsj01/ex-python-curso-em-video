from datetime import date

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CADASTRO DE TRABALHADOR EM PYTHON '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

cadastro = dict()
cadastro['nome'] = input('Nome: ').capitalize()
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

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-090 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

aluno = dict()

aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'.upper()
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'.upper()
else:
    aluno['situacao'] = 'Reprovado'.upper()
print('-=' * 30)
for chave, valor in aluno.items():
    print(f'  - {chave} é igual a {valor}')

# ---------------------------------------------

'''aluno = dict()

aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
print(f'  - nome é igual a {aluno["nome"]}')
print(f'  - média é igual a {aluno["media"]}')
print(f'  - situação é igual a {aluno["situacao"].upper()}')'''

# ---------------------------------------------

'''aluno = {}

aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
print('  - nome é igual a', aluno['nome'])
print('  - média é igual a', aluno['media'])
print('  - situação é igual a', aluno['situacao'].upper())'''
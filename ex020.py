#O método shuffle() pega uma sequência, como uma lista, e reorganiza a ordem dos itens.
from random import shuffle

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' SORTEANDO UMA ORDEM DA LISTA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

cont = 1
lista_alunos = []

while cont <= 4:
    lista_alunos.append(input('{}° aluno: '.format(cont)))
    cont += 1

shuffle(lista_alunos)
print('A ordem de apresentação será\n{}'.format(lista_alunos))

#aluno_um = input('Primeiro aluno: ')
#aluno_dois = input('Segundo aluno: ')
#aluno_tres = input('Terceiro aluno: ')
#aluno_quatro = input('Quarto aluno: ')

#lista_alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
#shuffle(lista_alunos)
#print('A ordem de apresentação será\n{}'.format(lista_alunos))

#print('A ordem de apresentação será')
#print(lista_alunos)

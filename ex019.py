# O método choice() retorna um elemento selecionado aleatoriamente da sequência especificada.
from random import choice

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' SORTEANDO UM ITEM NA LISTA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

cont = 1
lista_alunos = []

while cont <= 4:
    lista_alunos.append(input('{}° aluno: '.format(cont)))
    cont += 1

aluno_escolhido = choice(lista_alunos)
print('O aluno escolhido foi {}.'.format(aluno_escolhido))

#aluno_um = input('Primeiro aluno: ')
#aluno_dois = input('Segundo aluno: ')
#aluno_tres = input('Terceiro aluno: ')
#aluno_quatro = input('Quarto aluno: ')

#lista_alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
#aluno_escolhido = choice(lista_alunos)
#print('O aluno escolhido foi {}.'.format(aluno_escolhido))

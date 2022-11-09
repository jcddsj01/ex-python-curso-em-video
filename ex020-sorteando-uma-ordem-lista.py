cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'vermelho': '\033[1;41m',
    'verde': '\033[1;42m',
    'amarelo': '\033[1;43m',
    'azul': '\033[1;44m',
    'roxo': '\033[1;45m',
    'azulclaro': '\033[1;46m',
    'cinza': '\033[1;47m'
}

print('+', '-' * 8, '+')
print('| {} EX-020 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

#O método shuffle() pega uma sequência, como uma lista, e reorganiza a ordem dos itens.
from random import shuffle

count = 1
lista_alunos = []

while count <= 4:
    lista_alunos.append(input('{}° aluno: '.format(count)))
    count += 1

shuffle(lista_alunos)
print('A ordem de apresentação será\n{}'.format(lista_alunos))

# -------------------------------------------------------

#from random import shuffle

#aluno_um = input('Primeiro aluno: ')
#aluno_dois = input('Segundo aluno: ')
#aluno_tres = input('Terceiro aluno: ')
#aluno_quatro = input('Quarto aluno: ')

#lista_alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
#shuffle(lista_alunos)
#print('A ordem de apresentação será\n{}'.format(lista_alunos))

#print('A ordem de apresentação será')
#print(lista_alunos)



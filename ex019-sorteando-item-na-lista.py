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
print('| {} EX-019 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

#O método choice() retorna um elemento selecionado aleatoriamente da sequência especificada.
from random import choice

count = 1
lista_alunos = []

while count <= 4:
    lista_alunos.append(input('{}° aluno: '.format(count)))
    count += 1

aluno_escolhido = choice(lista_alunos)
print('O aluno escolhido foi {}.'.format(aluno_escolhido))

# --------------------------

#from random import choice

#aluno_um = input('Primeiro aluno: ')
#aluno_dois = input('Segundo aluno: ')
#aluno_tres = input('Terceiro aluno: ')
#aluno_quatro = input('Quarto aluno: ')

#lista_alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
#aluno_escolhido = choice(lista_alunos)
#print('O aluno escolhido foi {}.'.format(aluno_escolhido))
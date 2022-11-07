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
print('| {} EX-007 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

primeira_nota = float(input('Primeira nota do aluno: '))
segunda_nota = float(input('Segunda nota do aluno: '))
media_nota = (primeira_nota + segunda_nota) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(primeira_nota, segunda_nota, media_nota))

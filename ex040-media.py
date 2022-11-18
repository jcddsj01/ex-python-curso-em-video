cores_texto = {
    'limpa': '\033[m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m'
}

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'vermelho': '\033[1;47m'
}

titulo = ' EX-040 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

titulo = ' ESCOLA - CURSO EM VIDEO '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['vermelho'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')

primeira_nota = float(input('Primeira nota: '))
segunda_nota = float(input('Segunda nota: '))
media = (primeira_nota + segunda_nota) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(primeira_nota, segunda_nota, media))
if media >= 7:
    print('{}O aluno está APROVADO.{}'.format(cores_texto['verde'], cores_texto['limpa']))
elif media >= 5:
    print('{}O aluno está em RECUPERAÇÃO{}'.format(cores_texto['amarelo'], cores_texto['limpa']))
else:
    print('{}O aluno está REPROVADO{}'.format(cores_texto['vermelho'], cores_texto['limpa']))
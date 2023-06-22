cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' MÉDIA ARITMÉTICA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

primeira_nota = float(input('Primeira nota do aluno: '))
segunda_nota = float(input('Segunda nota do aluno: '))
media_nota = (primeira_nota + segunda_nota) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(primeira_nota, segunda_nota, media_nota))

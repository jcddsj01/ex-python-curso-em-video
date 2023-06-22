cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CONTANDO VOGAIS EM TUPLA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+')

palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra.lower()}', end=' ')
print()

'''palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra in 'aáãâeéêiou':
            print(f'{letra.lower()}', end=' ')
print()'''

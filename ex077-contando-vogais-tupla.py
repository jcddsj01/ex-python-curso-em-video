cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-077 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

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

# -----------------------------------------

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

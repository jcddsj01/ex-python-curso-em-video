cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-083 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

expressao = str(input('Digite a expressão: ')).strip()
pilha = list()
for simbolo in expressao:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

# ---------------------------------------------

'''expressao = str(input('Digite a expressão: ')).strip()
countEsq = 0
countDir = 0
for item in expressao:
    if item == '(':
        countEsq += 1
    if item == ')':
        countDir += 1
if countEsq == countDir:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')'''

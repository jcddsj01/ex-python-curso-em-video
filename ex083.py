cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' VALIDANDO EXPRESSÕES MATEMÁTICAS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

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

'''expressao = str(input('Digite a expressão: ')).strip()
contEsq = 0
contDir = 0
for item in expressao:
    if item == '(':
        contEsq += 1
    if item == ')':
        contDir += 1
if contEsq == countDir:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')'''

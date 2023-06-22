cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' UM PRINT ESPECIAL '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

def escreva(msg):
    t = len(msg) + 4
    print('~' * t)
    print(f'  {msg}')
    print('~' * t)

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')

'''def escreva(msg):
    t = len(msg) + 4
    print('~' * t)
    print(f'  {msg}')
    print('~' * t)

m = input('Digite um texto: ')
escreva(m)'''

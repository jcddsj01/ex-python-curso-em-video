cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))

print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))

print('A última letra A apareceu na posição {}'.format(frase.rfind('A') + 1))

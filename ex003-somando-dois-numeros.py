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
print('| {} EX-003 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

# Valores do tipo int sem casa decimal
valor_um = int(input('Digite um valor: '))
valor_dois = int(input('Digite outro valor: '))
soma = valor_um + valor_dois
print('A soma entre {} e {} é igual a {}!'.format(valor_um, valor_dois, soma))

# Valores do tipo float com casa decimal
#valor_um = float(input('Digite um valor: '))
#valor_dois = float(input('Digite outro valor: '))
#soma = valor_um + valor_dois
#print('A soma entre {} e {} é igual a {}!'.format(valor_um, valor_dois, soma))
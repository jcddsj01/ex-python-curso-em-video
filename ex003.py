cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' SOMANDO DOIS NÚMEROS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

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

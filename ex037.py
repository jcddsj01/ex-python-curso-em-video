cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

titulo = ' CONVERSOR DE BASES NUMÉRICAS '
print('+' + '-' * len(titulo) + '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+' + '-' * len(titulo) + '+')

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:].upper()))
else:
    print('Opção inválida! Tente novamente.')

'''print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO\n' + '[ 2 ] converter para OCTAL\n' + '[ 3 ] converter para HEXADECIMAL')'''

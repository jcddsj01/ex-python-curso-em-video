from time import sleep

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CRIANDO UM MENU DE OPÇÕES '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = valor1 + valor2
        print('O resultado de {} + {} é {}'.format(valor1, valor2, soma))
    elif opcao == 2:
        produto = valor1 * valor2
        print('O resultado de {} X {} é {}'.format(valor1, valor2, produto))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {} e {} o maior valor é {}'.format(valor1, valor2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')

'''from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

while True:
    print(#    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa)
    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = valor1 + valor2
        print('O resultado de {} + {} é {}'.format(valor1, valor2, soma))
    elif opcao == 2:
        produto = valor1 * valor2
        print('O resultado de {} X {} é {}'.format(valor1, valor2, produto))
    elif opcao == 3:
        maior = max(valor1, valor2)
        print('Entre {} e {} o maior valor é {}'.format(valor1, valor2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        print('=-=' * 10)
        break
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')'''

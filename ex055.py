cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' MAIOR E MENOR DA SEQUÊNCIA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

maior_peso = 0
menor_peso = 0
for pessoa in range(1, 5 + 1):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior peso lido foi de {}Kg'.format(maior_peso))
print('O maior peso lido foi de {}Kg'.format(menor_peso))

'''pesos = []
for count in range(1, 5 + 1):
    pesos.append(float(input('Peso da {}ª pessoa: '.format(count))))
print('O maior peso lido foi de {}Kg'.format(max(pesos)))
print('O menor peso lido foi de {}Kg'.format(min(pesos)))'''

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' ANALISADOR COMPLETO '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulheres_20 = 0

for pessoa in range(1, 4 + 1):
    print('_____ {}ª PESSOA _____'.format(pessoa))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if pessoa == 1 and sexo in 'M':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'F' and idade < 20:
        total_mulheres_20 += 1

media_idade = soma_idade / 2

print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome))
print('Ao todo são {} mulher(es) com menos de 20 anos.'.format(total_mulheres_20))

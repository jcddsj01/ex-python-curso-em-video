cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' UNINDO DICIONÁRIOS E LISTAS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

cadastro = list()
quantPessoas = 0
somaIdade = 0
mulheres = []
while True:
    nome = input('Nome: ').capitalize()
    while True:
        sexo = input('Sexo: [M/F]: ').upper()
        if sexo in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    if sexo == 'F':
        mulheres.append(nome)
    idade = int(input('Idade: '))
    somaIdade += idade
    cadastro.append({"nome": nome, "sexo": sexo, "idade": idade})
    quantPessoas += 1
    while True:
        continuar = input('Quer continuar? [S/N] ').upper()
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == "N":
        break
print('-=' * 35)
print(f'A) Ao todo temos {quantPessoas} pessoa(s) cadastrada(s).')
mediaIdade = somaIdade / quantPessoas
print(f'B) A média de idade é de {mediaIdade:.2f} anos.')
newMulheres = " ".join(mulheres)
print(f'C) A(s) mulher(es) cadastrada(s) foram {newMulheres}', end=' ')
print('\nD) Lista das pessoas que estão acima da média:')
for pessoa in cadastro:
    if pessoa["idade"] >= mediaIdade:
        print('     ', end='')
        for chave, valor in pessoa.items():
            print(f'{chave} = {valor};', end=' ')
        print()
print('<< ENCERRADO >>')

#galera = list()
#pessoa = dict()
#soma = media = 0
#while True:
#    pessoa.clear()
#    pessoa['nome'] = input('Nome: ')
#    while True:
#        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
#        if pessoa['sexo'] in 'MF':
#            break
#        print('ERRO! Por favor, digite apenas M ou F.')
#    pessoa['idade'] = int(input('Idade: '))
#    soma += pessoa['idade']
#    galera.append(pessoa.copy())
#    while True:
#        resp = input('Quer continuar? [S/N] ').upper()[0]
#        if resp in 'SN':
#            break
#        print('ERRO! Responda apenas S ou N.')
#    if resp == 'N':
#        break
#print('-=' * 35)
#print(f'A) Ao todo temos {len(galera)} pessoa(s) cadastrada(s).')
#media = soma / len(galera)
#print(f'B) A média de idade é de {media:.2f} anos.')
#print(f'C) A(s) mulher(es) cadastrada(s) foram ', end='')
#for pessoa in galera:
#    if pessoa["sexo"] in 'Ff':
#        print(f'{pessoa["nome"]} ', end='')
#print()
#print('D) Lista das pessoas que estão acima da média:')
#for p in galera:
#    if p['idade'] >= media:
#        print('     ', end='')
#        for c, v in p.items():
#            print(f'{c} = {v}; ', end='')
#        print()
#print('<< ENCERRADO >>')

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-065 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

count = 0
soma = 0
media = 0
maior = 0
menor = 0
resposta = 'S'
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    count += 1
    if count == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / count
print('Você digitou {} números e a média foi {}'.format(count, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
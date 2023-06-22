cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' MAIOR E MENOR VALORES '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
terceiro_valor = int(input('Terceiro valor: '))

menor = primeiro_valor
if segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    menor = segundo_valor
if terceiro_valor < primeiro_valor and terceiro_valor < segundo_valor:
    menor = terceiro_valor

maior = primeiro_valor
if segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    maior = segundo_valor
if terceiro_valor > primeiro_valor and terceiro_valor > segundo_valor:
    maior = terceiro_valor

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

'''primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
terceiro_valor = int(input('Terceiro valor: '))

print('O menor valor digitado foi {}'.format(min(primeiro_valor, segundo_valor, terceiro_valor)))
print('O maior valor digitado foi {}'.format(max(primeiro_valor, segundo_valor, terceiro_valor)))'''

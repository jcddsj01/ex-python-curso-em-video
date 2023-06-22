cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' DISSECANDO UMA VARIÁVEL '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
# print('Só tem espaços? ', ' ' in a)
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
# print('Está capitalizada? ', a[0].isupper())
print('Está capitalizada? ', a.istitle())

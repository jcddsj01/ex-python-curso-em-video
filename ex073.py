cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' TUPLAS COM TIMES DE FUTEBOL '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
         'Atlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
         'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
         'Cuiabá', 'Ceará-SC', 'Atlético-GO', 'Avaí', 'Juventude')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')

'''times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
         'Atlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
         'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
         'Cuiabá', 'Ceará-SC', 'Atlético-GO', 'Avaí', 'Juventude')

print('-=' * 20)
print('Lista de times do Brasileirão: ', end='')
for time in times:
    print(time, end=' - ')
print()
print('-=' * 20)
print('Os 5 primeiros são: ', end='')
for time in times[:5]:
    print(time, end=' - ')
print()
print('-=' * 20)
print('Os 4 últimos são: ', end='')
for time in times[-4:]:
    print(time, end=' - ')
print()
print('-=' * 20)
print('Times em ordem alfabética: ', end='')
for time in sorted(times):
    print(time, end=' - ')
print()
print('-=' * 20)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')'''

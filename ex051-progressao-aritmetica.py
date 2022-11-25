cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-051 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

titulo2 = '   10 TERMOS DE UMA PA   '
print('=' * len(titulo2))
print(titulo2)
print('=' * len(titulo2))

pa = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = pa + (10 - 1) * razao
for count in range(pa, decimo + razao, razao):
    print('{}'.format(count), end=' -> ')
print('Acabou')

# --------------------------

'''pa = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
count = 1
while count <= 10:
    if count < 10:
        print('{}'.format(pa), end=' -> ')
    elif count == 10:
        print('{}'.format(pa), end=' -> ')
    pa += razao
    count += 1
print('Acabou')'''
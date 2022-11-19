cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-046 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

from time import sleep

for count in range(10, -1, -1):
    print(count)
    sleep(1)
print('BUM! BUM! POOOW!')

# --------------------------

'''count = 10
while count >= 0:
    print(count)
    sleep(1)
    count -= 1
print('BUM! BUM! POOOW!')'''
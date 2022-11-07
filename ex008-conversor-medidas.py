cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'vermelho': '\033[1;41m',
    'verde': '\033[1;42m',
    'amarelo': '\033[1;43m',
    'azul': '\033[1;44m',
    'roxo': '\033[1;45m',
    'azulclaro': '\033[1;46m',
    'cinza': '\033[1;47m'
}

print('+', '-' * 8, '+')
print('| {} EX-008 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

medida = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a'.format(medida))

quilometro = medida / 1000
hectometro = medida / 100
decametro = medida / 10
decimetro = medida * 10
centimetro = medida * 100
milimetro = medida * 1000

print('{}km'.format(quilometro))
print('{}hm'.format(hectometro))
print('{}dam'.format(decametro))
print('{:.0f}dm'.format(decimetro))
print('{:.0f}cm'.format(centimetro))
print('{:.0f}mm'.format(milimetro))

# --------------------------------

#medida = float(input('Uma distância em metros: '))
#print('A medida de {}m corresponde a'.format(medida))
#print('{}km'.format(medida / 1000))
#print('{}hm'.format(medida / 100))
#print('{}dam'.format(medida / 10))
#print('{:.0f}dm'.format(medida * 10))
#print('{:.0f}cm'.format(medida * 100))
#print('{:.0f}mm'.format(medida * 1000))
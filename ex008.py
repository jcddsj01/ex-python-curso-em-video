cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CONVERSOR DE MEDIDA '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

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

#medida = float(input('Uma distância em metros: '))
#print('A medida de {}m corresponde a'.format(medida))
#print('{}km'.format(medida / 1000))
#print('{}hm'.format(medida / 100))
#print('{}dam'.format(medida / 10))
#print('{:.0f}dm'.format(medida * 10))
#print('{:.0f}cm'.format(medida * 100))
#print('{:.0f}mm'.format(medida * 1000))

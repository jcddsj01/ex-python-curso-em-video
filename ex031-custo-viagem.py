cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-031 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')

distancia_viagem = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distancia_viagem))
if distancia_viagem <= 200:
    preco_viagem = distancia_viagem * 0.50
else:
    preco_viagem = distancia_viagem * 0.45

#preco_viagem = distancia_viagem * 0.50 if distancia_viagem <= 200 else distancia_viagem * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(preco_viagem))
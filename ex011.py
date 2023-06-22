cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' PINTANDO PAREDE '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura

# Cada litro de tinta, pinta uma área de 2m²
litros_tinta = area / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(litros_tinta))

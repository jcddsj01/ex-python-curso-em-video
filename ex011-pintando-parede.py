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
print('| {} EX-011 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura

# Cada litro de tinta, pinta uma área de 2m²
litros_tinta = area / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(litros_tinta))
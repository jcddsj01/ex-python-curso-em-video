cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'verde': '\033[1;42m'
}

titulo = ' EX-042 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

titulo = ' Analisador de Triângulos V2.0 '

print('+', '=' * len(titulo), '+')
print('| {}{}{} |'.format(cores_fundo['verde'], titulo, cores_fundo['limpa']))
print('+', '=' * len(titulo), '+')

seg_a = float(input('Primeiro segmento: '))
seg_b = float(input('Segundo segmento: '))
seg_c = float(input('Terceiro segmento: '))

if seg_a < seg_b + seg_c and seg_b < seg_a + seg_c and seg_c < seg_a + seg_b:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if seg_a == seg_b == seg_c:
        print('EQUILÁTERO')
    elif seg_a != seg_b != seg_c != seg_a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo')

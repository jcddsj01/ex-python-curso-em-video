cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m',
    'verde': '\033[1;42m'
}

cabecalho = ' ANALISANDO TRIÂNGULO V1.0 '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

seg_a = float(input('Primeiro segmento: '))
seg_b = float(input('Segundo segmento: '))
seg_c = float(input('Terceiro segmento: '))

if seg_a < seg_b + seg_c and seg_b < seg_a + seg_c and seg_c < seg_a + seg_b:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo')

from math import radians, sin, cos, tan

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' SENO, COSSENO E TANGENTE '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

angulo = float(input('Digite o ângulo que você deseja: '))

#converte o angulo para radianos e depois com esse angulo em radianos converte para seno
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

#converte o angulo para radianos e depois com esse angulo em radianos converte para cosseno
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))

#converte o angulo para radianos e depois com esse angulo em radianos converte para tangente
tangente = tan(radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))

cores_texto = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;7;30m',
    'vermelho': '\033[1;31m',
    'amarelo': '\033[1;33m'
}

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' RADAR ELETRÔNICO '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('{}MULTADO! Você excedeu o limite permitido que é de 80Km/h{}'.format(cores_texto['vermelho'], cores_texto['limpa']))
    print('{}Você deve pagar uma multa de{} {}R${:.2f}!{}'.format(cores_texto['vermelho'], cores_texto['limpa'], cores_texto['amarelo'], multa, cores_texto['limpa']))
else:
    print('{}Tenha um bom dia! Dirija com segurança!{}'.format(cores_texto['amarelo'], cores_texto['limpa']))

'''
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('{}MULTADO! Você excedeu o limite permitido que é de 80Km/h{}'.format(cores_texto['vermelho'], cores_texto['limpa']))
    print('{}Você deve pagar uma multa de{} {}R${:.2f}!{}'.format(cores_texto['vermelho'], cores_texto['limpa'], cores_texto['amarelo'], multa, cores_texto['limpa']))
print('{}Tenha um bom dia! Dirija com segurança!{}'.format(cores_texto['amarelo'], cores_texto['limpa']))
'''

cores_texto = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;7;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'azulclaro': '\033[1;36m',
    'cinza': '\033[1;37m'
}

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
print('| {} EX-029 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('{}MULTADO! Você excedeu o limite permitido que é de 80Km/h{}'.format(cores_texto['vermelho'], cores_fundo['limpa']))
    print('{}Você deve pagar uma multa de{} {}R${:.2f}!{}'.format(cores_texto['vermelho'], cores_fundo['limpa'], cores_texto['amarelo'], multa, cores_texto['limpa']))
else:
    print('{}Tenha um bom dia! Dirija com segurança!{}'.format(cores_texto['amarelo'], cores_texto['limpa']))

# ---------------------------------------------------------

'''
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('{}MULTADO! Você excedeu o limite permitido que é de 80Km/h{}'.format(cores_texto['vermelho'], cores_fundo['limpa']))
    print('{}Você deve pagar uma multa de{} {}R${:.2f}!{}'.format(cores_texto['vermelho'], cores_fundo['limpa'], cores_texto['amarelo'], multa, cores_texto['limpa']))
print('{}Tenha um bom dia! Dirija com segurança!{}'.format(cores_texto['amarelo'], cores_texto['limpa']))
'''
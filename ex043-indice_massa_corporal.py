cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'roxo': '\033[1;35m'
}

titulo = ' EX-043 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

titulo = ' IMC - ÍNDICE DE MASSA CORPÓREA '

print('+', '=' * len(titulo), '+')
print('| {}{}{} |'.format(cores_fundo['roxo'], titulo, cores_fundo['limpa']))
print('+', '=' * len(titulo), '+')

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal, cuidado!')
elif imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc < 30:
    print('Você está em SOBREPESO, cuidado!')
elif imc < 40:
    print('Você está em OBESIDADE, cuidado!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

# -------------------------------------

'''if imc < 18.5:
    print('Você está ABAIXO DO PESO normal, cuidado!')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO, cuidado!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')'''
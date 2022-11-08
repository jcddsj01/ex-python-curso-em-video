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
print('| {} EX-014 {} |'.format(cores_fundo['pretoebranco'], cores_fundo['limpa']))
print('+', '-' * 8, '+')

#formula
#(C x 9/5) + 32

celcius = float(input('Informe a temperatura em °C: '))
#ordem de precedencia
fahrenheit = 9 * celcius / 5 + 32
#fahrenheit = ((9 * celcius) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(celcius, fahrenheit))


cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' CONVERSOR DE TEMPERATURAS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

celcius = float(input('Informe a temperatura em °C: '))
#ordem de precedencia
fahrenheit = 9 * celcius / 5 + 32
#fahrenheit = ((9 * celcius) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(celcius, fahrenheit))

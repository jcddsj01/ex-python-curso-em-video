cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].capitalize() == 'Sua cidade')

#separa_cidade = cidade.split()

#if separa_cidade[0].capitalize() == 'Sua cidade':
#    print(True)
#else:
#    print(False)

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-034 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')

salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    aumento = salario + (salario * (15 / 100))
else:
    aumento = salario + (salario * (10 / 100))
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumento))
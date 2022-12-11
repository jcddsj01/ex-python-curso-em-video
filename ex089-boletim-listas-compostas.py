cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m'
}

titulo = ' EX-088 '
print('+' + '-' * len(titulo) + '+')
print('|{}{}{}|'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+' + '-' * len(titulo) + '+')
print()

boletim = list()
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resposta in 'Nn':
        print('-=' * 30)
        print(f'{"Nº":<4}{"NOME":<13}{"MÉDIA":>8}')
        print('-' * 30)
        break
for indice, aluno in enumerate(boletim):
    print(f'{indice:<4}{aluno[0]:<13}{aluno[2]:>8.1f}')
print('-' * 30)
while True:
    resposta = int(input('Mostrar notas de qual aluno(a)? (999 INTERROMPE): '))
    if resposta != 999 or resposta != len(boletim) - 1:
        resposta = int(input(f'Opção inválida! Digite um valor válido: '))
    if resposta == 999:
        print('FINALIZANDO...')
        print('<' * 3, 'VOLTE SEMPRE', '>' * 3)
        break
    if resposta <= len(boletim) - 1:
        print(f'As notas de {boletim[resposta][0]} são: {boletim[resposta][1]}')
        print('-' * 30)

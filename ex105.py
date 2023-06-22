from statistics import mean

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' ANALISANDO E GERANDO DICIONÁRIOS '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação do aluno(a).
    :param n: Uma ou várias notas do aluno(a).
    :param sit: Valor OPCIONAL que indica se deve ou não adicionar a situação do aluno(a).
    :return: Dicionário com as informações do aluno(a).
    """
    aluno = dict()
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = mean(n)
    if sit:
        if aluno['media'] >= 7:
            aluno['situacao'] = 'BOA'
        elif aluno['media'] >= 5:
            aluno['situacao'] = 'RAZOÁVEL'
        else:
            aluno['situacao'] = 'RUIM'
    return aluno
print('-' * 40)
resp = notas(8, 7.5, 9, 10, sit=True)
print(resp)
# help(notas)

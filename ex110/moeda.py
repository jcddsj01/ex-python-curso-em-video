def metade(preco=0, formato=False):
    calc = preco / 2
    return calc if formato is False else moeda(calc)

def dobro(preco=0, formato=False):
    calc = preco * 2
    return calc if formato is False else moeda(calc)

def aumentar(preco=0, taxa=0, formato=False): 
    calc = preco + (taxa / 100 * preco)
    return calc if not formato else moeda(calc)

def diminuir(preco=0, taxa=0, formato=False):
    calc = preco - (taxa / 100 * preco)
    return calc if not formato else moeda(calc)

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxa_aumento=0, taxa_reducao=0):
    titulo = 'RESUMO DO VALOR'
    print('-' * 30)
    print(titulo.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(preco)}')
    print(f'Dobro do preço:\t\t{dobro(preco, True)}')
    print(f'Metade do preço:\t{metade(preco, True)}')
    print(f'{taxa_aumento}% de aumento:\t\t{aumentar(preco, taxa_aumento, True)}')
    print(f'{taxa_reducao}% de redução:\t\t{diminuir(preco, taxa_reducao, True)}')
    print('-' * 30)

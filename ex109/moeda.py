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

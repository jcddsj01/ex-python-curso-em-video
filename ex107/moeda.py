def metade(preco):
    calc = preco / 2
    return calc

def dobro(preco):
    calc = preco * 2
    return calc

def aumentar(preco, taxa):
    calc = preco + (preco * taxa / 100)
    return calc

def diminuir(preco, taxa):
    calc = preco - (preco * taxa / 100)
    return calc
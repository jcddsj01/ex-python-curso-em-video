def leiaDinheiro(msg):
    while True:
        preco_str = input(msg).replace(',', '.').strip()
        if preco_str.isalpha() or preco_str == '':
            print(f'\033[1;31mERRO! "{preco_str}" não um preço válido!.\033[m')
        else:
            return float(preco_str)

# def leiaDinheiro(msg):
#     while True:
#         preco_str = input(msg).replace(',', '.').strip()
#         if not preco_str.replace('.', '').isdigit():
#             print(f'\033[1;31mERRO! "{preco_str}" não é um preço válido!\033[m')
#         else:
#             return float(preco_str)

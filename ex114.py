import urllib.error
import urllib.request

class Cores:
    SEM_COR = '\033[m'
    PRETO_BRANCO = '\033[1;40m'


def cabecalho(texto, cor):
    linha = '-' * len(texto)
    print(f'\n{cor}+{linha}+{Cores.SEM_COR}')
    print(f'{cor}|{texto}|{Cores.SEM_COR}')
    print(f'{cor}+{linha}+{Cores.SEM_COR}\n')


cabecalho(' SITE ESTÁ ACESSÍVEL? ', Cores.PRETO_BRANCO)

try:
    response = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento.")
else:
    print("Consegui acessar o site com sucesso!")

# ---------------------------------------------------

# import requests
#
# try:
#     response = requests.get('http://pudim.com.br/')
# except requests.ConnectionError:
#     print("O site Pudim não está acessível no momento.")
# else:
#     print("Consegui acessar o site com sucesso!")

# ---------------------------------------------------

# import urllib.error
# import urllib.request
#
# url = input('Digite ou cole o link: ')
#
# try:
#     response = urllib.request.urlopen(url)
# except urllib.error.URLError:
#     print("O site Pudim não está acessível no momento.")
# else:
#     print("Consegui acessar o site com sucesso!")

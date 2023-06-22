import urllib.error
import urllib.request

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' SITE ESTÁ ACESSÍVEL? '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

try:
    response = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento.")
else:
    print("Consegui acessar o site com sucesso!")

# import requests
#
# try:
#     response = requests.get('http://pudim.com.br/')
# except requests.ConnectionError:
#     print("O site Pudim não está acessível no momento.")
# else:
#     print("Consegui acessar o site com sucesso!")

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

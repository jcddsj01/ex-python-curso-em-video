import pygame

cores_fundo = {
    'limpa': '\033[m',
    'preto_branco': '\033[1;40m'
}

cabecalho = ' TOCANDO UM MP3 '
print('+', '-' * len(cabecalho), '+')
print(f"| {cores_fundo['preto_branco']}{cabecalho}{cores_fundo['limpa']} |")
print('+', '-' * len(cabecalho), '+', '\n')

def reproduzir_audio(arquivo, volume=1.0):
    pygame.mixer.init()
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    print('Reproduzindo ...')
    while pygame.mixer.music.get_busy():
        pass
    print('Áudio finalizado.')


# Exemplo de uso 1 para o arquivo nesse diretório
arquivo_audio = "audio/audio.mp3"

# Exemplo de uso 2 para o arquivo em outro diretório
# arquivo_audio = r"C:\Users\seu-nome-de-usuário\Music\audio.mp3"

# Exemplo de uso 1 para controle de volume
volume = 0.3 # Valor entre 0.0 e 1.0 para controlar o volume (0.0 = mínimo, 1.0 = máximo)

reproduzir_audio(arquivo_audio, volume)

# Exemplo de uso 2 para controle de volume
# reproduzir_audio(arquivo_audio, volume=0.3)

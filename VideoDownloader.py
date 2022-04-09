__author__ = "Quach"
__version__ = "1.2"
__status__ = "development"
__email__ = "quach.vrc@gmail.com"
__github__ = "https://github.com/QuachRTX"

import os
from pathlib import Path
from pytube import YouTube
from pytube.cli import on_progress

#text_end = '\033[38;2;255;00;31m'
#text_titles = '\033[38;1;255;00;92m'
#text_download = '\033[38;2;255;00;255m'   #  color as hex #FF00FF
#reset_color = '\033[39m'

print("############# VIDEO DOWNLOADER #############\n")

print("Digite a URL do video...")
url = input()
my_video = YouTube(url, on_progress_callback=on_progress)

print("\nDigite 1 para efetuar o download do video")
print("Digite 2 para efetuar o download do audio")
escolha = int(input())

print("\n*********** Titulo do Video ***********")
print(my_video.title,"\n")

print("*********** Thumbnail ***********")
print(my_video.thumbnail_url,"\n")

if escolha == 1:

    print("*********** Download Video ***********")
    print("Downloading...")

    my_video = my_video.streams.get_highest_resolution() 
    
    Path(f"{os.environ['UserProfile']}\Desktop\VideoDownloader\Videos").mkdir(parents=True, exist_ok=True)
    my_video.download(f"{os.environ['UserProfile']}\Desktop\VideoDownloader\Videos")

    print("\nDownload completo!")
elif escolha == 2:

    print("*********** Download Audio ***********")
    print("Downloading...")

    my_video = my_video.streams.get_audio_only()

    Path(f"{os.environ['UserProfile']}\Desktop\VideoDownloader\Audios").mkdir(parents=True, exist_ok=True)
    my_video.download(f"{os.environ['UserProfile']}\Desktop\VideoDownloader\Audios")

    print("\nDownload completo!")
else:
    print("Valor invalido!\n")

print("Pressione qualquer tecla para terminar..")
input()
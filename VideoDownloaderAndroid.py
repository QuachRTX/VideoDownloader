__author__ = "Quach"
__version__ = "1.2"
__status__ = "development"
__email__ = "quach.vrc@gmail.com"
__github__ = "https://github.com/QuachRTX"

#import androidhelper
import os
from pathlib import Path
from pytube import YouTube
from pytube.cli import on_progress
#droid = androidhelper.Android()

text_end = '\033[38;2;255;00;31m'
text_titles = '\033[38;1;255;00;92m'
text_download = '\033[38;2;255;00;255m'   #  color as hex #FF00FF
reset_color = '\033[39m'

print(text_titles,"############# VIDEO DOWNLOADER ANDROID #############\n")

print("Digite a URL do video...")
url = input()
my_video = YouTube(url, on_progress_callback=on_progress)

print("\nDigite 1 para efetuar o download do video")
print("Digite 2 para efetuar o download do audio")
escolha = int(input())

print(text_titles, "\n*********** Titulo do Video ***********")
print(my_video.title,"\n")

print("*********** Thumbnail ***********")
print(my_video.thumbnail_url,"\n")

if escolha == 1:

    print("*********** Download Video ***********", reset_color)
    print(text_download, "Downloading...")

    my_video = my_video.streams.get_highest_resolution() 
    
    Path(r"/storage/emulated/0/VideoDownloader/Videos").mkdir(parents=True, exist_ok=True)
    my_video.download(f"/storage/emulated/0/VideoDownloader/Videos")

    #droid.makeToast('Download completo!')
    print("\nDownload completo!", reset_color)
elif escolha == 2:

    print(text_titles,"*********** Download Audio ***********",reset_color)
    print(text_download,"Downloading...")

    my_video = my_video.streams.get_audio_only()

    Path(r"/storage/emulated/0/VideoDownloader/Audios").mkdir(parents=True, exist_ok=True)
    my_video.download(f"/storage/emulated/0/VideoDownloader/Audios")

    #droid.makeToast('Download completo!')
    print("\nDownload completo!",reset_color)
else:
    print(text_end,"Valor invalido!\n",reset_color)

print(text_end,"Pressione qualquer tecla para terminar..",reset_color)
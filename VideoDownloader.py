__author__ = "Quach"
__version__ = "1.5"
__status__ = "development"
__email__ = "quach.vrc@gmail.com"
__github__ = "https://github.com/QuachRTX"

import os
import sys
import pyfiglet
from pathlib import Path
from pytube import YouTube
from pytube.cli import on_progress

VIDEO_DIR = os.path.join(os.environ['UserProfile'], 'Desktop', 'VideoDownloader', 'Videos')
AUDIO_DIR = os.path.join(os.environ['UserProfile'], 'Desktop', 'VideoDownloader', 'Audios')

def download_video(url):
    try:
        my_video = YouTube(url, on_progress_callback=on_progress).streams.get_highest_resolution()
        Path(VIDEO_DIR).mkdir(parents=True, exist_ok=True)
        my_video.download(VIDEO_DIR)
        print("\nDownload completo!")
    except:
        print("\nFalha ao baixar o vídeo. Certifique-se de que a URL está correta e tente novamente.")
        sys.exit()

def download_audio(url):
    try:
        my_video = YouTube(url, on_progress_callback=on_progress).streams.get_audio_only()
        Path(AUDIO_DIR).mkdir(parents=True, exist_ok=True)
        my_video.download(AUDIO_DIR)
        print("\nDownload completo!")
    except:
        print("\nFalha ao baixar o áudio. Certifique-se de que a URL está correta e tente novamente.")
        sys.exit()

def print_video_info(video):
    try:
        print("\n*********** Título do vídeo ***********")
        print(video.title)
        print("\n*********** Thumbnail ***********")
        print(video.thumbnail_url)
    except:
        print("\nFalha ao carregar o título e/ou thumbnail do vídeo.")

def main():
    title = pyfiglet.figlet_format("VideoDownloader 1.5", font="slant", width=100)
    print(title)

    print("Digite a URL do vídeo...")
    url = input()

    try:
        video = YouTube(url, on_progress_callback=on_progress)
        print_video_info(video)
    except:
        print("\nFalha ao carregar o vídeo. Certifique-se de que a URL está correta e tente novamente.")
        sys.exit()

    print("\nDigite 'v' para baixar o vídeo, 'a' para baixar o áudio ou 's' para sair...")
    download_type = input()

    if download_type == 's' or download_type == 'S':
        sys.exit()
    elif download_type == 'v' or download_type == 'V':
        download_video(url)
    elif download_type == 'a' or download_type == 'A':
        download_audio(url)
    else:
        print("\nOpção inválida. Tente novamente.")
        main()


if __name__ == '__main__':
    main()
 

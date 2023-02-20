import pafy
from youtubesearchpython import VideosSearch
from colorama import Fore, Style

song_names = input("Enter the song names: ")

song_names_split = song_names.split(",")

for song in song_names_split:
    result = [video['link']
              for video in VideosSearch(song, limit=1).result()['result']]
    final_result = result[0]

    url = pafy.new(final_result)
    print(
        f"Downloading {Fore.YELLOW}{url.title} By {url.author}{Style.RESET_ALL}...")
    media = url.getbestaudio() 
    media.download()

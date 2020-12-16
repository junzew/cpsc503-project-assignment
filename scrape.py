import os
import requests
from bs4 import BeautifulSoup

"""
Scrapes the Longman online dictionary to download audio files
for 1000 basic English words
"""

f1 = open('1000words.txt')

MP3 = '.mp3'
DOWNLOAD_DIR = 'download_1000/'

def get_audio_url(word):
    html_text = requests.get("https://www.ldoceonline.com/dictionary/{}".format(word),
                             headers={"User-Agent":"Mozilla/5.0"}).text
    soup = BeautifulSoup(html_text, 'html.parser')
    url = soup.find('span', {"class": "amefile"})['data-src-mp3']
    return url


def download_mp3(word, url, dir_path):
    print(word, url, dir_path)
    filename = os.path.join(dir_path, word + MP3)
    with open(filename, 'wb') as file:
        file.write(requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).content)


for word in f1.readlines():
    word = word[:-1]
    try:
        url = get_audio_url(word)
        download_mp3(word, url, DOWNLOAD_DIR)
    except Exception as e:
        print(e)

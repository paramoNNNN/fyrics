import sys
import requests
from glob import glob
from bs4 import BeautifulSoup
from optparse import OptionParser
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, USLT
from mutagen.id3 import ID3NoHeaderError

# SettingUp Options
parser = OptionParser()
parser.add_option("-p", "--path", dest="path",
                  help="path of your music folder", metavar="path")

parser.add_option("-r", "--recursive", action="store_true", dest="recursive",
                  help="traverse all subdirectories", metavar="recursive")
option, args = parser.parse_args()

if option.path is None:
    raise Exception("You must set path to your Music folder. use -h/--help to show help message")
else:
    path = option.path if option.path.endswith("/") else option.path + "/"

if option.recursive is not None:
    recursive = True
else:
    recursive = False

def find(artist, title, file):
    session = requests.session()

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = "https://www.musixmatch.com/lyrics/" + artist.replace(' ', '-') + "/" + title.replace(' ', '-')
    response = session.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    lyrics = ""
    items = soup.findAll('p', {'class': 'mxm-lyrics__content'})
    if len(items) == 0:
        print("\033[91m" + "No lyrics found for " + artist + " - " + title +
              "\n" + "URL: " + url + "\033[0m")
        return

    for item in items:
        lyrics += item.text

    print("Adding lyrics for " + artist + " - " + title)
    try:
        tags = ID3(file)
    except ID3NoHeaderError:
        print("\033[91m" + "No ID3 header found for " + artist + " - " + title + "\033[0m")

    tags['USLT::eng'] = (USLT(encoding=3, lang='eng', text=lyrics))
    tags.save(file)
    print("Lyrics successfully added for " + artist + " - " + title)


if recursive:
    items = glob(path + "**/*.mp3", recursive=True)
else:
    items = glob(path + "*.mp3")

for item in items:
    tags = ID3(item)
    title = str(tags["TIT2"])
    artist = str(tags["TPE1"])

    find(artist=artist, title=title, file=item)
    print("\n \n")


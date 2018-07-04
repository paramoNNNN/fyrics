## Fyrics
Embed lyrics into Audio File


### Requirements
- [Python3.x](https://www.python.org/downloads/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  `pip3 install beautifulsoup4`
- [Requests](http://docs.python-requests.org/en/master/)
  `pip3 install requests`
- [Mutagen](https://mutagen.readthedocs.io/en/latest/)
`pip3 install mutagen`

### Options
* **-p/--path** `path to your Music folder`

* **-r/--recursive** `traverse all subdirectories`

* **-h/--help** `show help message`

### Installation
* **Linux, Windows**:

  Just install requirments and [Python3.x](https://www.python.org/downloads/) and run the Script from Terminal/PowerShell

* **Android**:

  Coming Soon

### Examples
* **Album Folder**:

  ```python3 fyrics.py -p /home/taha/Music/A Perfect Circle/2003 - Thirteenth Step```

* **Artist Folder**:

  ```python3 fyrics.py -r -p /home/taha/Music/A Perfect Circle/```
  
### TODO
- [ ] Set lyrics manually
- [ ] Add more Sources to find lyrics
- [ ] Support Android

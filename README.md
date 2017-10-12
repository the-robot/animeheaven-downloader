**Anime Heaven Downloader**  
> Author: *Ghost* [official.ghost@tuta.io](mailto:official.ghost@tuta.io)  
> **README:** this is not official, and dev for this script is nothing related with Anime Heaven team. It was written by myself  just to download anime episodes easily. Anime episodes credit go to [Anime Heaven](http://animeheaven.eu/).  


**How To Use**  
- go to [Anime Heaven](http://animeheaven.eu/), select the anime you want and open one episode  
- copy the url and remove **&e=....**  
- paste the copied url in the script and enter the episode[s] you want to download, check the screenshot below  
![screenshot](https://raw.githubusercontent.com/Hadesy2k/ahdownloader/master/screenshot.png)


**Changes**
- updated the script to parse dynamic HTML content for video url

---
### Run with Python3

**Create command shortcut**
- move the `ahdownloader.py` to `/usr/share/` or `/usr/local/bin/` for Mac
- write the follow bash script in `/usr/bin/` or `/usr/local/bin/` for Mac
	- replace `/usr/share/` with `/usr/local/bin/` for Mac 
```
#!/bin/bash
python3 /usr/share/ahdownloader.py "$@"
```

**Lib Requirements**  
- [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4)  
- [ProgressBar](https://pypi.python.org/pypi/progressbar2)  
- [Selenium](https://pypi.python.org/pypi/selenium)
- [PhamtomJS](http://phantomjs.org/)

**Lib Installation for Ubuntu**
- `sudo pip3 install beautifulsoup4 selenium`
- `sudo apt-get install python3-progressbar`
- `npm -g install phamtomjs-prebuilt`
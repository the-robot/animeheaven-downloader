**Anime Heaven Downloader**
> **README:** this is not official, and dev for this script is nothing related with Anime Heaven team. It was written by myself  just to download anime episodes easily. Anime episodes credit go to [Anime Heaven](http://animeheaven.eu/).  


**Changes**
- codebase is refactored
- add logger methods, modularized the code so it can be reused in other automated scripts (see `WHY` at the bottom)
- add animeheaven request blocked handling
- remove the use of progressbar2, and use custom simple progressbar
- way of using the program changed, see [How To Use](https://github.com/the-robot/animeheaven-downloader/blob/master/README.md#how-to-use)

---

### Run with Python3

**Lib Requirements**  
- [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4)
- [Selenium](https://pypi.python.org/pypi/selenium)
- [PhantomJS](http://phantomjs.org/)

**Lib Installation for Ubuntu**
- `sudo pip3 install beautifulsoup4 selenium`
- `npm -g install phantomjs-prebuilt`

---

### How To Use

- go to [Anime Heaven](http://animeheaven.eu/), and simply copy the anime overview page
	- i.e. [http://animeheaven.eu/i.php?a=Bakuman.](http://animeheaven.eu/i.php?a=Bakuman.)
- python app.py --anime={ANIME URL} --episode={1-10}

> --episode: can be either single episode (1) or range (1-10)

> --download: optional parameter to set download path. i.e. --download='/Users/anime/Desktop'

---

### WHY THE HECK IS THIS GUY REFACTORED THE CODE

- First of all, the whole purpose of writing this is to save my time from browsing the site and clicking one by one
- After few weeks, people from Anime Heaven added "Abuse Blocking Method"
- So either way I have to change my code to work, but also I am planning to reuse this code in my other automated script
	- interested? I will give you an idea
	- simple way is write schedule tasks with [Celery](http://www.celeryproject.org)
	- if you have Raspberry Pi and FTP server running on local for storage, run celery on Raspberry and use FTP to save your downloaded videos there
	- so if you want to watch the new episode of anime, just FTP into yours and enjoy!
	

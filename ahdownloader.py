"""
Author: Ghost (official.ghost@tuta.io)
Readme:
    This is unofficial, and not related with Anime Heaven.
    It is written just for convinient, feel free to share or edit
    Animes are credited to AnimeHeaven.eu
"""

import urllib.request, urllib.error
from progressbar import ProgressBar, Percentage, Bar, RotatingMarker, ETA, FileTransferSpeed
import re
from bs4 import BeautifulSoup


class Downloader:
    def __init__(self, url, epRange):
        """ url -> string
            episode -> string (from-to) """
        self.downloads = []
        self.pbar = ""  # Download Progressbar

        self.Main(url, epRange)

    def Main(self, url, epRange):
        """ Main Method """
        # get download urls
        print("[-] Getting episodes urls")
        for each in self.getRange(epRange):  # Episode Range
            html = self.fetchUrl(url + "&e=" + str(each))
            if html != None:
                self.scrapeDownLink(html)
            else:
                print("[404] url not found for episode " + str(each))

        # download files
        print("[-] Downloading process started\n")
        for each in self.downloads:
            filename = each.split("/")[-1]
            self.downloadFile(each, filename)
        print("\n[+] All episodes successfully downloaded")

    def getRange(self, epRange):
        """ return list of numbers (range) from given str format (min-max) """
        epRange = list(map(int, epRange.split('-')))
        if len(epRange) > 1:
        	return list(range(epRange[0], epRange[1]+1))
        else:
        	return epRange

    def fetchUrl(self, url):
        """ return website source code """
        try:
            connection = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
            #print(e.code) FOR DEBUG
            return None
        except urllib.error.URLError as e:
            #print('URLError') FOR DEBUG
            return None
        else:
            return connection.read()

    def scrapeDownLink(self, html):
        """ scrap the download link from the given HTML source """
        soup = BeautifulSoup(html, "html.parser")
        for each in soup.find_all('div', class_='mirrorsa2'):
            self.getDownloads(str(each))

    def getDownloads(self, html):
        """ get download link from the scrapped html source with Regex """
        regex = r"href='(.*?)'>"
        for link in re.findall(regex, html):
            if 'animeheaven.eu/video' in link:  # remove query ?dd and add to downloads
                self.downloads.append(link.replace("?dd", ""))

    def downloadFile(self, url, filename):
        """ download the video """
        self.setProgressBar(filename)
        urllib.request.urlretrieve(url, filename, reporthook=self.progressBar)
        self.pbar.finish()

    def setProgressBar(self, filename):
        """ Reset Progressbar """
        self.pbar = ProgressBar(widgets=[filename.replace(".mp4", " "), Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ', FileTransferSpeed()])

    def progressBar(self, count, blockSize, totalSize):
        if self.pbar.maxval is None:
            self.pbar.maxval = totalSize
            self.pbar.start()
        self.pbar.update(min(count*blockSize, totalSize))


def banner():
    print("Anime Heaven Downloader by Ghost (github.com/Hadesy2k/ahdownloader)")
    print("Check above url for how to use the script.\n")

if __name__ == "__main__":
    banner()

    try:
        anime = input("Enter Anime Url (with http): ")
        epRange = input("Enter episode no. or in range [from-to]: ")
        print("")
        Downloader(anime, epRange)
    except KeyboardInterrupt:
        exit()

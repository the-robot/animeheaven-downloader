"""
Author: Ghost (official.ghost@tuta.io)
Readme:
    This is unofficial, and not related with Anime Heaven.
    It is written just for convinient, feel free to share or edit
    Animes are credited to AnimeHeaven.eu

https://github.com/hadesy2k/ahdownloader
"""


import urllib.request
import re
from collections import OrderedDict

from bs4 import BeautifulSoup
from progressbar import ProgressBar, Percentage, Bar, RotatingMarker, ETA, FileTransferSpeed
from selenium import webdriver


class Downloader:
    def __init__(self, url, epRange):
        """ url -> string
            episode -> string (from-to) """
        self.driver = webdriver.PhantomJS()
        self.downloads = OrderedDict()  # sort episodes in asending order
        self.pbar = ""  # Download Progressbar
        self.Main(url, epRange)

    def Main(self, url, epRange):
        """ Main Method """
        print("[-] Getting episodes urls")
        for episode_number in self.getRange(epRange):  # Episode Range
            html = self.fetchUrl(url + "&e=" + str(episode_number))
            if html != None:
                self.getDownload(html, episode_number)
            else:
                print("[404] url not found for episode " + str(episode_number))

        print("[-] Downloading process started\n")
        for filename, url in self.downloads.items():
            self.downloadFile(filename, url)
        print("\n[+] Finished downloading. Enjoy your anime.")

    def getRange(self, epRange):
        """ return list of numbers (range) from given str format (min-max) """
        epRange = list(map(int, epRange.split('-')))
        if len(epRange) > 1:
            return list(range(epRange[0], epRange[1]+1))
        else:
            return epRange

    def fetchUrl(self, url):
        """ return website source code """
        self.driver.get(url)
        html = self.driver.page_source
        return html

    def getDownload(self, html, episode_number):
        """ scrap the download link from the given HTML source """
        soup = BeautifulSoup(html, "html.parser")
        download = soup.find_all('source')
        if download:
            self.downloads["Episode %s.mp4" % str(episode_number)] = download[0]['src']
            return

        print("[!] Download link not found for episode %s" % str(episode_number))

    def downloadFile(self, filename, url):
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
    print("Anime Heaven Downloader by Ghost (https://github.com/Hadesy2k/ahdownloader)")
    print("Check above url for how to use the script.\n")


if __name__ == "__main__":
    banner()

    try:
        anime = input("Enter Anime Url (with http): ")
        epRange = input("Enter episode no. or in range [from-to]: ")
        Downloader(anime, epRange)
    except KeyboardInterrupt:
        exit()

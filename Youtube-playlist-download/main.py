__author__ = 'deepanshu'

import requests
from bs4 import BeautifulSoup
from urllib import request
import os


def get_url():
    """This method basically is to take a url input from user"""

    url = ''

    while True:
        while True:
            url = input("Enter url: ")
            if len(url):
                break
        try:
            response = request.urlopen(url)
            break
        except ValueError:
            print("Unknown URL try again")
        except:
            print("Something is wrong exciting program")
            exit(1)

    return url


def spider(given_url):
    """This method is the core of the program"""
    
    url_to_crawl = given_url

    source_code = requests.get(url_to_crawl)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    # name = soup.find('h1', {'class': 'pl-header-title'})
    # name = name.string
    # name = str(name)
    # name = name.strip('')
    # fw = open('links of' + name + '.txt', 'w')
    # fw2 = open('names of' + name + '.txt', 'w')
    fw = open('links.txt', 'w')
    fw2 = open('names.txt', 'w')
    for link in soup.findAll('a', {'class': 'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link '}):
        my_href = 'https://www.youtube.com' + link.get('href')
        title = link.string
        #print(my_href, title)
        fw.write(my_href + '\n')
        fw2.write(title)

    fw.close()
    fw2.close()

    """Downloading Part"""
    try:
        os.system("youtube-dl --max-quality FORMAT -a links.txt")
        return
    except:
        print("Something went wrong related to downloading")
        exit(2)


if __name__ == '__main__':
    spider(get_url())

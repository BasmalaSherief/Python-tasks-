#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

link = requests.get("https://ipinfo.io/").content
soup = BeautifulSoup(link,"lxml")
print(soup)




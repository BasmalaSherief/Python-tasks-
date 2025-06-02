#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

link = requests.get("https://ipinfo.io/").content
soup = BeautifulSoup(link,'html.parser')

print(f"All data you can get by your Public ip {soup}")


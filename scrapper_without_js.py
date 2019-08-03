# pip install beautifulsoup4

import requests
import csv
from bs4 import BeautifulSoup
import json
import time

s = requests.Session()


# GET
url = "https://www.example.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
}

r = s.get(url, headers=headers)

# POST
server = 'us7'
url = 'https://www.example.com/'

payload = {
    'cook': 'on'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
}

cookies = {
    'PHPSESSID': r.cookies['PHPSESSID']
}

r = s.post(url, data=json.dumps(payload), headers=headers, cookies=cookies)

import requests
from bs4 import BeautifulSoup
import urllib.request


url = 'https://hasaki.vn/danh-muc/cham-soc-da-mat-high-end-c1909.html?p='
max_numpage = 2
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(soup)
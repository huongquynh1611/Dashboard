import requests
from bs4 import BeautifulSoup
import urllib.request
max_num_page = 1

url_tail = '&shopCollection=101112932&sortBy=pop'
url = 'https://shopee.vn/hasaki.vn?page=' + str(max_num_page) + url_tail

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

print(soup)
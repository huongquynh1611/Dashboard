
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date


def crawl(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    page_content = soup.find(id='list_sp_col_right')
    items = page_content.find_all("div", class_="item_sp_hasaki width_common relative")
    item_name = None
    item_brand = None
    item_id = None
    data = []
    today = None
    for item in items:
        item_href            = item.find_all('a')[0]['href']
        item_page            = requests.get(item_href)
        item_soup            = BeautifulSoup(item_page.content,"html.parser")
        item_thong_so        = item_soup.find(id='box_thongsosanpham').tbody.findAll('tr')
        key_item   = []
        value_item = []
        for ths in item_thong_so:
            ths_key   = ths.find_all('td')[0].text.strip()
            ths_value = ths.find_all('td')[1].text.strip()
            key_item.append(ths_key)
            value_item.append(ths_value)
        dict_item_ths = dict(zip(key_item,value_item))


        item_name            = item.find_all('a')[1]['data-name']
        item_brand           = item.find_all('a')[1].get('data-brand', None)
        item_id              = item.find_all('a')[1]['data-id']
        
        data.append((item_name,item_brand,item_id,dict_item_ths))
    return data

    
data_main = []
max_numpage = 44
head_url = 'https://hasaki.vn/danh-muc/trang-diem-c23.html?p='
for i in range(1,max_numpage+1):
    
    url  = head_url + str(i)
    data   = crawl(url)
    data_main += data

df = pd.DataFrame(data_main,columns=['item_name','item_brand','item_id','item_thong_so'])
df.to_excel('information_trang_diem.xlsx')
    

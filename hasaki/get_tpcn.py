
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
    item_variant = None
    item_product = None
    item_price = None
    item_bought = None
    item_discount = None
    item_price_previous = None
    item_star = None
    item_comment_number = None
    data = []
    today = None
    for item in items:
        today                = date.today()
        item_href            = item.find_all('a')[0]['href']
        item_name            = item.find_all('a')[1]['data-name']
        item_brand           = item.find_all('a')[1].get('data-brand', None)
        item_id              = item.find_all('a')[1]['data-id']
        item_variant         = item.find_all('a')[1]['data-variant']
        item_product         = item.find_all('a')[1]['data-product']
        item_price           = item.find_all('a')[1]['data-price']
        item_bought          = item.find('span',class_='item_count_by')
        if item_bought is not None:
            item_bought = item_bought.text.strip()
        item_discount        = item.find('span',class_='discount_percent2_deal')
        if item_discount is not None: 
            item_discount = item_discount.text.strip()
        item_price_previous  = item.find('span',class_='item_giacu txt_12 right')
        if item_price_previous is not None: 
            item_price_previous = item_price_previous.text.strip()
        item_star            = item.find('div',class_='number_start')
        if item_star is not None:
            item_star = item_star['style'].split(':')[-1].strip(';')
        item_comment_number  = item.find('div',class_='block_count_by width_common').text.strip()
    
        if '(' in item_comment_number:
            item_comment_number = item_comment_number.split('(')[-1].split(')')[0]
        else:
            item_comment_number = None
        data.append((item_name,item_brand,item_id,item_variant,item_product,item_price,item_bought,item_discount,item_price_previous,item_star,item_comment_number,today))
    return data

    
data_main = []
max_numpage = 4
head_url = 'https://hasaki.vn/danh-muc/thuc-pham-chuc-nang-c156.html?p='
for i in range(1,max_numpage+1):
    
    url  = head_url + str(i)
    data   = crawl(url)
    data_main += data

df = pd.DataFrame(data_main,columns=['item_name','item_brand','item_id','item_variant','item_product','item_price','item_bought','item_discount','item_price_previous','item_star','item_comment_number','date'])
df.to_excel('result_tpcn.xlsx')
    

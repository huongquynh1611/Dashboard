import requests
from bs4 import BeautifulSoup



max_numpage = 1
url = 'https://hasaki.vn/danh-muc/cham-soc-toc-c96.html?p=' + str(max_numpage)

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

for item in items:
    print('=============')
    # print(item.find_all('a')[0]['href'])
    item_name            = item.find_all('a')[1]['data-name']
    item_brand           = item.find_all('a')[1]['data-brand']
    item_id              = item.find_all('a')[1]['data-id']
    item_variant         = item.find_all('a')[1]['data-variant']
    item_product         = item.find_all('a')[1]['data-product']
    item_price           = item.find_all('a')[1]['data-price']
    item_bought          = item.find('span',class_='item_count_by').text.strip()
    item_discount        = item.find('span',class_='discount_percent2_deal').text.strip()
    item_price_previous  = item.find('span',class_='item_giacu txt_12 right').text.strip()
    item_star            = item.find('div',class_='number_start')
    if item_star is not None:
        item_start = item_star['style'].split(':')[-1].strip(';') 
    item_comment_number  = item.find('div',class_='block_count_by width_common').text.strip()
   
    if '(' in item_comment_number:
        item_comment_number = item_comment_number.split('(')[-1].split(')')[0]
    else:
        item_comment_number = None

    

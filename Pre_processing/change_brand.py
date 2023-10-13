import pandas as pd
df = pd.read_excel('information_full_data.xlsx')
new_brand = []

dict_brand = {"ANGEL":"ANGEL's LIQUID","L":"L'OREAL","IT":"IT'S SKIN","TEROSI D":"TEROSI D'ORIENTE","J":"J'WHITE","POND":"POND'S","KIEHL":"KIEHLS","SO":"SO'NATURAL","SHINA":"SHINA'S","NATURE":"NATURE'S BOUNTY"}
for _,i  in df.iterrows():

    item_brand = i['item_brand'].upper()
    brand = item_brand
    
    if item_brand in list(dict_brand.keys()):
    
        brand = dict_brand[item_brand]
    new_brand.append(brand)
df['New Brand'] = new_brand
df.to_excel('new_brand.xlsx')

    
    
    

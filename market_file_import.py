#trying to import all market items for sale in a station

import requests
import json
import pandas as pd
import numpy as np
from datetime import timedelta, date, datetime

Amarr = '10000043'
Hek = '10000042'
Jita = '10000002'
Rens = '10000030'
Dodixie = '10000032'

file = 'Amarr_MarketOrders_REV1.xlsx'
data = pd.ExcelFile(file)
types = data.parse(0)
print(type(data))

#item_list = requests.get(df1[0])
#json_list = item_list.json()

#print(type(json_list))
#print(json_list)
timeDiff = str(date.today() - timedelta(days=7))
def product_total_sold(number):
    url = 'https://esi.evetech.net/latest/markets/' + Amarr + '/history/?datasource=tranquility&type_id='+ str(number)
    region = requests.get(url)
    all_region_Markets = region.json()

    sales = []
    # find items sold per day
    for products_sold in all_region_Markets:
        print(products_sold['date'],' sales per day:', products_sold['volume'])
        #print(products_sold)
        if products_sold['date'] > timeDiff:
            sales.append(products_sold['volume'])

    weekly_sales= sum(sales)
    #print('Item Id: ' + str(number) ,'Weekly sales: ',weekly_sales)
    return weekly_sales

def product_total_added(number):
    url2 = 'https://esi.evetech.net/latest/markets/' + Amarr +'/orders/?datasource=tranquility&order_type=sell&page=1&type_id='+ str(number)
    daily_items = requests.get(url2)
    all_products = daily_items.json()

    # number of items on market per day
    volumes=[]
    # Find total items added to market in 7 days.
    for items_total in all_products:
        print('Items added per day:', items_total['volume_total'])
        if items_total['issued'] > timeDiff:
            volumes.append(items_total['volume_total'])

    weekly_vol= sum(volumes)
    #print('                 Items added: ', weekly_vol)
    return weekly_vol

count = 0
for type_id in types[:,0]:
    try:
        sold_items = product_total_sold(type_id)
        added_items = product_total_added(type_id)
        SVR= (sold_items/added_items)*100
    except:
        continue

    # Output SRV value
    if SVR >= 100:
        count += 1
        print('Item Id: ' + str(type_id) ,'Amarr Sales to Volume Ratio (%) =', int(SVR))

print('')
print(count,' Items')
print('')
print('End Items')

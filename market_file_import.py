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

def product_total_sold(number):
    url = 'https://esi.evetech.net/latest/markets/' + Amarr + '/history/?datasource=tranquility&type_id='+ str(number)
    region = requests.get(url)
    all_region_Markets = region.json()

    sales = []
    # find items sold per day
    for products_sold in all_region_Markets:
        #print(products_sold['date'], number,' sales per day:', products_sold['volume'])
        #print(products_sold)
        if products_sold['date'] > str(timeDiff):
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

        if items_total['issued'] > str(timeDiff):
            volumes.append(items_total['volume_total'])
            #print('Items added per day:', items_total['volume_total'])

    weekly_vol= sum(volumes)
    #print('Items added: ', weekly_vol)
    return weekly_vol

file = 'Market_Orders.csv'
data = pd.read_csv(file)
#print(data)


count = 0
timeDiff = date.today() - timedelta(days=7)
for type_id in data['TypeID']:
    #try excludes any sold_items/0 issues
    try:
        sold_items = product_total_sold(int(type_id))
        added_items = product_total_added(int(type_id))
        SVR= (sold_items/added_items)*100
    except:
        continue

    # Output SRV value
    if SVR >= 100:
        count += 1
        print('Item Id: ' + str(int(type_id)) + ' Amarr Sales to Volume Ratio (%) =', int(SVR))

print('')
print(count,' Items')
print('')
print('End Items')

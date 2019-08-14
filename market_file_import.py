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
    #print(all_region_Markets)

    sales = []
    # find items sold per day
    for products_sold in all_region_Markets:
        #print(products_sold['date'], number,' sales per day:', products_sold['volume'])
        #print(products_sold.keys())
        if products_sold['date'] > str(timeDiff):
            sales.append(products_sold['volume'])

    weekly_sales= sum(sales)
    #print('Item Id: ' + str(number) ,'Weekly sales: ',weekly_sales)
    return weekly_sales

def product_total_added(number):
    url2 = 'https://esi.evetech.net/latest/markets/' + Amarr +'/orders/?datasource=tranquility&order_type=sell&page=1&type_id='+ str(number)
    daily_items = requests.get(url2)
    all_products = daily_items.json()
    #print(all_products)
    # number of items on market per day
    volumes=[]
    # Find total items added to market in 7 days.
    for items_total in all_products:
        #print(items_total.keys())
        if items_total['issued'] > str(timeDiff):
            volumes.append(items_total['volume_total'])
            #print('Items added per day:', items_total['volume_total'])

    weekly_vol= sum(volumes)
    #print('Items added: ', weekly_vol)
    return weekly_vol

file = 'Market_Orders.csv'
data = pd.read_csv(file, index_col=0)
print(datetime.today())
#print(data.keys())
#print(type(data[['TypeID']]))
count = 0
timeDiff = date.today() - timedelta(days=14)
df = pd.DataFrame()
for type_id, item_name in data.iterrows():
    #try excludes any sold_items/0 issues
    try:
        sold_items = product_total_sold(int(type_id))
        added_items = product_total_added(int(type_id))
        SVR= (sold_items/added_items)*100
    except:
        continue

    # Output SVR value
    margin = ((float(item_name['Sell Price']) - float(item_name['Buy Price']))/float(item_name['Buy Price']))*100
    if SVR >= 100 and added_items >= 14 and margin > 10:
        count += 1
        #df2 = pd.DataFrame([type_id, item_name['Item'], int(SVR)])
        #print(df2)
        print(str(int(type_id)) + ': ' + item_name['Item'] + ' Amarr Sales to Volume Ratio (%) =', int(SVR))
        print('Margin = %.2f' % margin,'%')
        print('Total Sold:',sold_items,'Total Posted:',added_items)
#    else:
#        print(str(int(type_id)) + ': ' + item_name['Item'])

print(datetime.today())
#print(df)
print('')
print(count,' Items')
print('')
print('End Items')

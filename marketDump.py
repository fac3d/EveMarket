# I'm hoping to be able to calculate Sales to Volume ratios on items being sold at each station.\
# The program should allow you to see how fast items sell in station when station trading.
# This is the first Python program I've ever written. Don't laugh.
import requests
import json
import math
from datetime import timedelta

# setting the URL's. Going to do this better later on.
station_name = input('What station do you want to query?')

#region_id's
Amarr='10000043'
Dodixie='10000032'
Hek='10000042'
Jita='10000002'
Rens='10000030'

#location_id's
Amarr_hub='60008494'
Dodixie_hub='60011866'
Hek_hub='60005686'
Jita_hub='60003760'
Rens_hub='60004588'

# function to get the SRV calculation.
# Not calculating correctly. Pulling wrong values for sales and volume. Need to research API for this.
def product_total_sold():
    url = 'https://esi.evetech.net/latest/markets/10000043/history/?datasource=tranquility&type_id=34'
    region = requests.get(url)
    all_region_Markets = region.json()

    # number of items sold per day
    sales=[]

    # find items sold per day
    for products_sold in all_region_Markets:
        #print('sales per day:', products['volume'])
        print(products_sold['date'],' sales per day:', products_sold['volume'])
        #print(products_sold)
        if products_sold['date'] > date.today() - timedelta(days=7):
            sales.append(products_sold['volume'])

    avg_7day_sales= sum(sales)/7
    return avg_7day_sales
    
def product_total_daily():
    url2 = 'https://esi.evetech.net/latest/markets/10000043/orders/?datasource=tranquility&order_type=sell&page=1&type_id=34'
    daily_items = requests.get(url2)
    all_products = daily_items.json()

    # number of items on market per day
    volumes=[]
    
    # Find total items on market. 
    # THIS NEEDS A SERIOUS REWORK!
    for Items_total in all_products[-7:]:
        #print('Items per day:', all_products['volume_total'])
        print(Items_total['issued'],' sales per day:', Items_total['volume_total'])
        #print(Items_sold)
        volumes.append(Items_total['volume_total'])
        
        avg_7day_vol= sum(volumes)/7
        return avg_7day_vol

sold_items = product_total_sold()
number_items = product_total_daily()
SVR= (sold_items/number_items)*100
    
# Output SRV value
print(Station + ' Sales to Volume Ratio (%) =', SVR)

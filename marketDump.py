# I'm hoping to be able to calculate Sales to Volume ratios on items being sold at each station.\
# The program should allow you to see how fast items sell in station when station trading.
# This is the first Python program I've ever written. Don't laugh.
import requests
import json
from datetime import timedelta, date, datetime

# setting the URL's. Going to do this better later on.
#station_name = input('What station do you want to query?')

#region_id's
Amarr='10000043'
Dodixie='10000032'
Hek='10000042'
Jita='10000002'
Rens='10000030'

#location_id's (keeping these in here so I don't have to look them up again.)
Amarr_hub='60008494'
Dodixie_hub='60011866'
Hek_hub='60005686'
Jita_hub='60003760'
Rens_hub='60004588'

# function to get the SRV calculation.
# Calculating SVR by pulling total items sold for the week(product_total_sold) and total added for the week (product_total_added).
def product_total_sold():
    url = 'https://esi.evetech.net/latest/markets/' + Amarr + '/history/?datasource=tranquility&type_id=34'
    region = requests.get(url)
    all_region_Markets = region.json()

    # number of items sold per day
    sales=[]

    # find items sold per day
    #can't figure out datetime usage. Convert to iso?
    for products_sold in all_region_Markets:
        #print(products_sold['date'],' sales per day:', products_sold['volume'])
        #print(products_sold)
        if products_sold['date'] > str(date.today() - timedelta(days=7)):
            sales.append(products_sold['volume'])

    daily_sales= sum(sales)
    print(daily_sales)
    return daily_sales

def product_total_added():
    url2 = 'https://esi.evetech.net/latest/markets/' + Amarr +'/orders/?datasource=tranquility&order_type=sell&page=1&type_id=34'
    daily_items = requests.get(url2)
    all_products = daily_items.json()

    # number of items on market per day
    volumes=[]

    # Find total items added to market in 7 days.
    for items_total in all_products:
        print('Items added per day:', items_total['volume_total'])
        # Will this work with 'issued' being date and time format?
        print(type(items_total))
        if items_total['issued'] > str(datetime.today() - timedelta(days=7)):
            volumes.append(items_total['volume_total'])

        print(volumes)
        daily_vol= sum(volumes)
        return daily_vol

sold_items = product_total_sold()
added_items = product_total_added()
#SVR= (sold_items/added_items)*100

# Output SRV value
#print('Amarr Sales to Volume Ratio (%) =', SVR)

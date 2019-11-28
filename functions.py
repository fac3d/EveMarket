#
# Filename: functions.py
#

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

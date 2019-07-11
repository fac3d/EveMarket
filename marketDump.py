import requests
import json
import math

#Amarr='10000043'
#Dodixie=
#Hek=
#Jita=
#Rens=

def item_srv():

    url = 'https://esi.evetech.net/latest/markets/10000043/history/?datasource=tranquility&type_id=10631'

    region = requests.get(url)
    allMarkets = region.json()
    volumes=[]
    sales=[]
    for products in allMarkets[-7:]:
        #print(products['date'],' volume per day:', products['volume'])
        volumes.append(products['volume'])
        sales.append(products['order_count'])
    
    avg_7day_vol= sum(volumes)/7
    avg_7day_sales= sum(sales)/7
    SVR= (avg_7day_sales/avg_7day_vol)*100
    return SRV

print('')
print('Average 7-Day Volume=',avg_7day_vol)
print('Average 7-Day Sales=',avg_7day_sales)
print('Sales to Volume Ratio (%) =', SVR)
print('')
print('volume=',type(products['volume']))
print('allMarkets=',type(allMarkets))
print('products=',type(products))

# I'm hoping to be able to calculate Sales to Volume ratios on items being sold at each station.\
# The program should allow you to see how fast items sell in station when station trading.
# This is the first Python program I've ever written. Don't laugh.
import requests
import json
import math

# setting the URL's. Going to do this better later on.
Amarr='https://esi.evetech.net/latest/markets/10000043/history/?datasource=tranquility&type_id=3536'
Dodixie='https://esi.evetech.net/latest/markets/10000032/history/?datasource=tranquility&type_id=17634'
Hek='https://esi.evetech.net/latest/markets/10000042/history/?datasource=tranquility&type_id=17634'
Jita='https://esi.evetech.net/latest/markets/10000002/history/?datasource=tranquility&type_id=17634'
Rens='https://esi.evetech.net/latest/markets/10000030/history/?datasource=tranquility&type_id=17634'

# function to get the SRV calculation.
# Not calculating correctly. Pulling wrong values for sales and volume. Need to research API for this.
def product_svr(station):
    url = station

    region = requests.get(url)
    allMarkets = region.json()
    volumes=[]
    sales=[]
    for products in allMarkets[-7:]:
        #print('sales per day:', products['order_count'])
        print(products['date'],' volume per day:', products['volume'])
        #print(products)
        volumes.append(products['volume'])
        sales.append(products['order_count'])

    avg_7day_sales= sum(sales)/7
    avg_7day_vol= sum(volumes)/7
    ratio= (avg_7day_sales/avg_7day_vol)*100
    
# ignore these. They are just for my sanity
    #print('')
    #print('Average 7-Day Sales=',avg_7day_sales)
    #print('Average 7-Day Volume=',avg_7day_vol)
    #print('')
    #print('volume=',type(products['volume']))
    #print('allMarkets=',type(allMarkets))
    #print('products=',type(products))
    
# this is the real value to return    
    return ratio

#this will change when I update the URL above
SVR_A = product_svr(Amarr)
#SVR_J = product_svr(Jita)
#SVR_R = product_svr(Rens)
#SVR_D = product_svr(Dodixie)
#SVR_H = product_svr(Hek)

# Output SRV value
print('Amarr Sales to Volume Ratio (%) =', SVR_A)
#print('Jita Sales to Volume Ratio (%) =', SVR_J)
#print('Rens Sales to Volume Ratio (%) =', SVR_R)
#print('Dodixie Sales to Volume Ratio (%) =', SVR_D)
#print('Hek Sales to Volume Ratio (%) =', SVR_H)

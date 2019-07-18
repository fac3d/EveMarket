# I'm hoping to be able to calculate Sales to Volume ratios on items being sold at each station.\
# The program should allow you to see how fast items sell in station when station trading.
# This is the first Python program I've ever written. Don't laugh.
import requests
import json
import math

# setting the URL's. Going to do this better later on.
Station=raw_input('What station do you want to query?')

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
def product_svr(Station):
    url = 'https://esi.evetech.net/latest/markets/'+Station+'/history/?datasource=tranquility&type_id=3536'

    region = requests.get(url)
    all_region_Markets = region.json()
    volumes=[]
    sales=[]
    for products in all_region_Markets[-7:]:
        #print('sales per day:', products['order_count'])
        #This isn't correct. Need to find another way to compute 'volume per day'.
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
    #print('allMarkets=',type(all_region_Markets))
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

import requests
import json
import math

Amarr='10000043'
#Dodixie=
#Hek=
#Jita=
#Rens=

url = 'https://esi.evetech.net/latest/markets/10000043/history/?datasource=tranquility&type_id=35'

region = requests.get(url)
allMarkets = region.json()

for products in allMarkets[-7:]:
    print(products['date'],' volume per day:', products['volume'])

print('')
print(type(products['volume']))
print('allMarkets=',type(allMarkets))
print('products=',type(products))

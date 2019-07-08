import requests
import json

#Amarr=
#Dodixie=
#Hek=
#Jita=
#Rens=

def (market_items)
url = 'https://esi.evetech.net/latest/markets/prices/?datasource=tranquility'

region = requests.get(url)
allMarkets = region.json()

#print(allMarkets)
#print('Volume:', data['volume'])
#print('Average:', data['average'])
#for k in data.keys():
#    print(k +':', data[k])
count=0
for i in allMarkets:
    count = count+1
for average_price in allMarkets:
    print(average_price)
print('')
print('Number of Items on New Eden Market: ',count)

market_items()

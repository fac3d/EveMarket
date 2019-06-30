import requests
import json

url = 'https://esi.evetech.net/latest/markets/10000003/history/?datasource=tranquility&type_id=34'

the_forge = requests.get(url)
data = the_forge.json()[0:1]
print(data)
#for key, value in data.item():
#    print('date +':', value )
    

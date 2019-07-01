import requests
import json

url = 'https://esi.evetech.net/latest/markets/10000003/types/?datasource=tranquility&page=1'

the_forge = requests.get(url)
data = the_forge.json()

print(data)
#print('Volume:', data['volume'])
#print('Average:', data['average'])
#for k in data.keys():
#    print(k +':', data[k])
count=0
for i in data:
    count = count+1
print('')
print('Number of Regional Items: ',count)

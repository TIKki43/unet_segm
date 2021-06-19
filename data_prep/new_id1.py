import matplotlib.pyplot as plt# Collect coords into list
import requests
import json
# node["name"~".*"]
'''
'building' = 'apartments, bungalow, cabin,detached,dormitory,farm,hotel,house,residential,commercial,industrial,office,kiosk,
retail,supermarket,warehouse, mosque,church,chapel,cathedral, civic, government, hospital,public, toilets, train_station,
transportation, kindergarten, school,  	university, college, grandstand, pavilion, sports_hall, stadium'
'''
import numpy as np
overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
(node['building' = 'apartments, bungalow, cabin,detached,dormitory,farm,hotel,house,residential,commercial,industrial,office,kiosk,
retail,supermarket,warehouse, mosque,church,chapel,cathedral, civic, government, hospital,public, toilets, train_station,
transportation, kindergarten, school,  	university, college, grandstand, pavilion, sports_hall, stadium'] (55.808896,49.086174,55.814612,49.106644); 
 way['building' = 'apartments, bungalow, cabin,detached,dormitory,farm,hotel,house,residential,commercial,industrial,office,kiosk,
retail,supermarket,warehouse, mosque,church,chapel,cathedral, civic, government, hospital,public, toilets, train_station,
transportation, kindergarten, school,  	university, college, grandstand, pavilion, sports_hall, stadium'](55.808896,49.086174,55.814612,49.106644);
 rel['building' = 'apartments, bungalow, cabin,detached,dormitory,farm,hotel,house,residential,commercial,industrial,office,kiosk,
retail,supermarket,warehouse, mosque,church,chapel,cathedral, civic, government, hospital,public, toilets, train_station,
transportation, kindergarten, school,  	university, college, grandstand, pavilion, sports_hall, stadium'](55.808896,49.086174,55.814612,49.106644);
);
out;
"""

response = requests.get(overpass_url,
                        params={'data': overpass_query})
data = response.json()

coords = []
for element in data['elements']:
  if element['type'] == 'node':
    lon = element['lon']
    lat = element['lat']
    coords.append((lon, lat))
  elif 'center' in element:
    lon = element['center']['lon']
    lat = element['center']['lat']
    coords.append((lon, lat))

X = np.array(coords)
print(len(X))

plt.plot(X[:, 0], X[:, 1], 'o')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis('equal')
plt.show()
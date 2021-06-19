import matplotlib.pyplot as plt  # Collect coords into list
import requests
# from PIL import Image 56.206010,47.229596,56.210534,47.245893
import json
# node["name"~".*"]
import pandas as pd

import numpy as np
overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
way["building"~".*"](55.486897,49.639865,55.491504,49.656163);  
(._;>;);
out;

"""

# overpass_query = """
# [out:json];
# (node["amenity"="building"](55.808945,49.086185,55.814660,49.106655);
#  way["amenity"="building"](55.808945,49.086185,55.814660,49.106655);
#  rel["amenity"="building"](55.808945,49.086185,55.814660,49.106655);
# );
# out;
# """
response = requests.get(overpass_url,
                        params={'data': overpass_query})
data = response.json()
# for i in data['elements']:
    # print(i)

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
print(X, len(X))
b = X

plt.plot(X[:, 0], X[:, 1], 'o')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis('equal')
# plt.imshow(img,zorder=0,  extent=[0.1, 10.0, -10.0, 10.0])
plt.show()

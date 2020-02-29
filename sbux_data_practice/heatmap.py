import folium
import pandas as pd
import json
from folium import plugins

# read in the coordinates data file
df = pd.read_csv('starbucksInLACounty.csv')

# read in the LA map json file to highlight LA county
with open('laMap.geojson') as f:
    laArea = json.load(f)


# initialize the LA County map
laMap = folium.Map(location=[34.0522, -118.2437], tiles='Stamen Toner', zoom_start=9)

# add the shape of LA County to the map
folium.GeoJson(laArea).add_to(laMap)

# for each row in the Starbucks dataset, plot the corresponding latitude and longitude on the map
for i, row in df.iterrows():
    folium.CircleMarker((row.latitude, row.longitude), radius=3, weight=2, color='red',
                        fill_color='red', fill_opacity=.5).add_to(laMap)

# add the heatmap. The core parameters are:
# --data: a list of points of the form (latitude, longitude) indicating locations of Starbucks stores

# --radius: how big each circle will be around each Starbucks store

# --blur: the degree to which the circles blend together in the heatmap

laMap.add_child(plugins.HeatMap(data=df[['latitude', 'longitude']].values, radius=25, blur=10))

# save the map as an html
laMap.save('laHeatmap.html')

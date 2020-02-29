import folium
import pandas as pd
import json

# read in the coordinates data file
df = pd.read_csv('starbucksInLACounty.csv')

# read in the LA map json file to highlight LA county
with open('laMap.geojson') as f:
    laArea = json.load(f)

# initialize the map around LA County
# location centers the map to LA (default is world map)
# tiles changes the display
# zoom_start is an int that zooms in the map (bigger int means more zoomed in)

# laMap = folium.Map(location=[34.0522, -118.2437], tiles='Stamen Toner', zoom_start=9)
laMap = folium.Map(location=[34.0522, -118.2437], tiles='OpenStreetMap', zoom_start=9)


# add the shape of LA County to the map
folium.GeoJson(laArea).add_to(laMap)

# for each row in the Starbucks data set, plot the corresponding latitude and longitude on the map
for i, row in df.iterrows():
    folium.CircleMarker((row.latitude, row.longitude), radius=3, weight=2, color='red',
                        fill_color='red', fill_opacity=.5).add_to(laMap)

# save the map as an html
laMap.save('laPointMap.html')

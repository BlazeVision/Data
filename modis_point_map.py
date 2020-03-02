import folium
import pandas as pd
import json

# read in the coordinates data file
df = pd.read_csv('MODIS_ThisYear.csv')

# read in the us_states json file to highlight the United States
with open('us_states_map.json') as f:
    us_states = json.load(f)

# initialize the map around the United States
# location centers the map to LA (default is world map)
# tiles changes the display
# zoom_start is an int that zooms in the map (bigger int means more zoomed in)

us_map = folium.Map(location=[40.141809, -100.298400], tiles='OpenStreetMap', zoom_start=4)

# add the shape of the US to the map
folium.GeoJson(us_states).add_to(us_map)

# for each row in the Starbucks data set, plot the corresponding latitude and longitude on the map
for i, row in df.iterrows():
    folium.CircleMarker((row.latitude, row.longitude), radius=0.2, weight=2, color='red',
                        fill_color='red', fill_opacity=.5).add_to(us_map)

# save the map as an html
us_map.save('usPointMap.html')

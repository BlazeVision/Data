import folium
import pandas as pd
import json

# read in the coordinates data file
df = pd.read_csv('starbucksInLACounty.csv')

# read in the LA map json file to highlight LA county
with open('laMap.geojson') as f:
    laArea = json.load(f)

# group the starbucks data frame by zip code and count the number of stores in each zip code
numStoresSeries = df.groupby('zip').count().id

# initialize an empty data frame to store this new data
numStoresByZip = pd.DataFrame()

# populate the new data frame with a 'zip code' column and a 'numStores' column
numStoresByZip['zipCode'] = [str(i) for i in numStoresSeries.index]
numStoresByZip['numStores'] = numStoresSeries.values

# initialize the LA County map
laMap = folium.Map(location=[34.0522, -118.2437], tiles='Stamen Toner', zoom_start=9)

# draw the choropleth map. These are the key components:
# --geo_data: the geojson which you want to draw on the map [in our case it is the zip codes in LA County]

# --data: the pandas data frame which contains the zip code information
# AND the values of the variable you want to plot on the choropleth

# --columns: the columns from the data frame that you want to use
# [this should include a geospatial column [zip code] and a variable [numStores]

# --key_on: the common key between one of your columns and an attribute in the geojson.
# This is how python knows which data frame row matches up to which zip code in the geojson

laMap = folium.Choropleth(geo_data='laZips.geojson', data=numStoresByZip, columns=['zipCode', 'numStores'],
                          key_on='feature.properties.zipcode', fill_color='YlGn', fill_opacity=1).add_to(laMap)

laMap.save('laChoropleth.html')

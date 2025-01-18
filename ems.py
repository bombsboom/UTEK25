import pandas as pd
import folium
import webbrowser

latlng = [34.0549, -118.2426]

#Initialize map
m = folium.Map(latlng, zoom_start=10)

#Read report database and add markers to map
reports = pd.read_csv('reports.csv')
reports = reports.reset_index()

#Feature groups for each damage type
Road = folium.FeatureGroup(name="Road Damage", show=True).add_to(m)

Building = folium.FeatureGroup(name="Building Collapsed", show=True).add_to(m)

Water = folium.FeatureGroup(name="Water Disconnected", show=True).add_to(m)

Electricity = folium.FeatureGroup(name="Electricity Disconnected", show=True).add_to(m)

Gas = folium.FeatureGroup(name="Gas Disconnected", show=True).add_to(m)

for index,row in reports.iterrows():
    if row['road'] == 1:
        folium.Marker(location = [row['latitude'],row['longitude']]).add_to(Road)

    if row['building'] == 1:
        folium.Marker(location = [row['latitude'],row['longitude']]).add_to(Building)

    if row['water'] == 1:
        folium.Marker(location = [row['latitude'],row['longitude']]).add_to(Water)

    if row['electricity'] == 1:
        folium.Marker(location = [row['latitude'],row['longitude']]).add_to(Electricity)

    if row['gas'] == 1:
        folium.Marker(location = [row['latitude'],row['longitude']]).add_to(Gas)

#Add region map ?


#Add layer controls to map
folium.LayerControl().add_to(m)

#Display map as webpage
m.save("map2.html")
webbrowser.open("map2.html",new=2)
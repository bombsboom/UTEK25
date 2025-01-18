import pandas as pd
import folium
import webbrowser
import requests
import json

latlng = [34.0549, -118.2426]

#Initialize map
m = folium.Map(latlng, zoom_start=10)

#Read report database and add markers to map
reports = pd.read_csv('reports.csv')
reports = reports.reset_index()

#Feature groups for each damage type
Road = folium.FeatureGroup(name="Road Damage", show=True).add_to(m)

Building = folium.FeatureGroup(name="Building Collapsed", show=False).add_to(m)

Water = folium.FeatureGroup(name="Water Disconnected", show=False).add_to(m)

Electricity = folium.FeatureGroup(name="Electricity Disconnected", show=False).add_to(m)

Gas = folium.FeatureGroup(name="Gas Disconnected", show=False).add_to(m)

for index,row in reports.iterrows():
    if row['road'] == 1:
        folium.Marker(location = [row['latitude'],row['longitude']]).add_to(Road)
        print("road")

    if row['building'] == 1:
        folium.Marker(location = [row['latitude'],row['longitude']]).add_to(Building)
        print("b")

    if row['water'] == 1:
        folium.Marker(location = [row['latitude'],row['longitude']]).add_to(Water)
        print("w")

    if row['electricity'] == 1:
        folium.Marker(location = [row['latitude'],row['longitude']]).add_to(Electricity)
        print("e")

    if row['gas'] == 1:
        folium.Marker(location = [row['latitude'],row['longitude']]).add_to(Gas)
        print("g")

zipmap = json.load(open("assets/map.json"))
magnitude = pd.read_csv(open("assets/magnitude.csv"))
folium.Choropleth(
    name="Report amounts County",
    geo_data=zipmap,
    data=magnitude,
    columns=["Zip", "Reports"],
    key_on="feature.properties.ZIPCODE",
    fill_color="YlGn",
).add_to(m)

#Add layer controls to map
folium.LayerControl().add_to(m)

#Display map as webpage
m.save("map2.html")
webbrowser.open("map2.html",new=2)
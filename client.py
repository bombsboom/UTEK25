from geopy.geocoders import Nominatim
import folium
import webbrowser

print("========================================================================")
print("This tool is for reporting infrastructure damage to emergency responce crews.\nIf you or someone you know is experiencing an emergency, call emergency services.")
print("========================================================================")

print("")

print("Input your address:\n")
address = input()

geolocator = Nominatim(user_agent="UTEK25")
location = geolocator.geocode(address)
latlng = [location.latitude,location.longitude]

print("Is your address " + location.address + "\n")

if input() == 'Y' or 'Yes' or 'y':

else:
    
print("Is there road blockage / damage at your location? (Y/N)\n")

road = input()
if building == 'Y' or 'Yes' or 'y':
    road = 1
else:
    road = 0

print("Is there a collapsed building at your location? (Y/N)\n")

building = input()
if building == 'Y' or 'Yes' or 'y':
    building = 1
else:
    building = 0

print("Is water running at your location? (Y/N)\n")

water = input()
if water == 'Y' or 'Yes' or 'y':
    water = 1
else:
    water = 0

print("Is electricity running at your location? (Y/N)\n")

electricity = input()
if electricity == 'Y' or 'Yes' or 'y':
    electricity = 1
else:
    electricity = 0

print("Is gas working at your location? (Y/N)\n")

gas = input()
if gas == 'Y' or 'Yes' or 'y':
    gas = 1
else:
    gas = 0

m = folium.Map(latlng, zoom_start=13)

folium.CircleMarker(
    location=latlng,
    radius=25,
    fill=True,
    popup=folium.Popup("inline explicit Popup"),
).add_to(m)

m.save("map2.html")
webbrowser.open("map2.html",new=2)
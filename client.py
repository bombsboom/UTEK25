import geocoder
import folium
import webbrowser

location = geocoder.ip('me').latlng

m = folium.Map(location, zoom_start=13)

folium.CircleMarker(
    location=location,
    radius=25,
    fill=True,
    popup=folium.Popup("inline explicit Popup"),
).add_to(m)

m.save("map2.html")
webbrowser.open("map2.html",new=2)
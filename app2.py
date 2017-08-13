import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name_list = list(data["NAME"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name_list):
  fg.add_child(folium.Marker(location=[lt, ln], popup = name + ", " + str(el) + "m",
  icon=folium.Icon(color="green")))


map.add_child(fg)

map.save("Map.html")

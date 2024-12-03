import folium
from OBA.bysykkel_api import get_all_stations
from OBA.credentials import credentials
import requests

_headers = {
    "Client-Identifier": credentials["user_id"]
}

response = get_all_stations(_headers)
stations = response['data']['stations']
oslo_coords = [59.9139, 10.7522]
bike_map = folium.Map(location=oslo_coords, zoom_start=13)

for station in stations:
    folium.Marker(
        location=[station['lat'], station['lon']],
        popup=f"<b>{station['name']}</b><br>Capacity: {station['capacity']}",
        icon=folium.Icon(color="blue", prefix="fa")
    ).add_to(bike_map)

bike_map.save("oslo_bikeshare_map.html")
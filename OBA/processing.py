import geopandas as gpd
from credentials import credentials
from bysykkel_api import get_all_stations, get_bike_info
import pandas as pd

_DATA_PATH = "data/oslo_bydeler_befolkning_2024.geojson"

_headers = {
    "Client-Identifier": credentials["user_id"]
    }

def load_arealer_gdf() -> gpd.GeoDataFrame:
    arealer_gdf = gpd.read_file(_DATA_PATH)
    return arealer_gdf

def load_stations_gdf() -> gpd.GeoDataFrame:
    response = get_all_stations(_headers)
    stations = response['data']['stations']
    stations_gdf = gpd.GeoDataFrame(stations)
    return stations_gdf

def load_availability_gdf(_headers) -> pd.DataFrame:
    availabiliy_info = get_bike_info(_headers)
    availability_df = pd.DataFrame(availabiliy_info['data']['stations'])
    return availability_df


def match_stations_and_availability(stations_gdf, availability_gdf) -> gpd.GeoDataFrame:
    stations_gdf = stations_gdf.merge(availability_gdf, left_on="station_id", right_on="station_id")
    stations_gdf = gpd.GeoDataFrame(stations_gdf, geometry=gpd.points_from_xy(stations_gdf.lon, stations_gdf.lat))
    stations_gdf.crs = "EPSG:4326"
    return stations_gdf



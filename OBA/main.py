import writer as wf
from mapbox_func import set_up_map, highlight_area
from plotting import generate_bike_stat, generate_area_stat, generate_stat_avg_
from credentials import credentials
from processing import load_arealer_gdf, load_stations_gdf, match_stations_and_availability, load_availability_gdf

_headers = {
    "Client-Identifier": credentials["user_id"]
    }

def _state_set_up_map(state):
    arealer_gdf = load_arealer_gdf()
    stations_gdf = load_stations_gdf()
    availability_gdf = load_availability_gdf(_headers)
    stations_gdf = match_stations_and_availability(stations_gdf, availability_gdf)
    state["bike_map"] = set_up_map(arealer_gdf, stations_gdf)

def _set_up_plots(state):
    arealer_gdf = load_arealer_gdf()
    stations_gdf = load_stations_gdf()
    availability_gdf = load_availability_gdf(_headers)
    stations_gdf = match_stations_and_availability(stations_gdf, availability_gdf)
    state["bike_stat"] = generate_bike_stat(stations_gdf, arealer_gdf)
    state["area_stat"] = generate_area_stat(arealer_gdf)
    state["stat_avg"] = generate_stat_avg_(arealer_gdf)

def _state_highlight_area(state, selected_bydel):
    state["bike_map"] = highlight_area(state["arealer_gdf"], state["bike_map"], selected_bydel)
    
initial_state = wf.init_state({
    "my_app": {
        "title": "MY APP"
    },
})

_state_set_up_map(initial_state)
#_set_up_plots(initial_state)
import writer as wf
import plotly.express as px
from bysykkel_api import get_all_stations
from credentials import credentials
import plotly.express as px
import pandas as pd
# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://dev.writer.com/framework

# Shows in the log when the app starts
print("Hello world!")

# Its name starts with _, so this function won't be exposed
def _update_message(state):
    is_even = state["counter"] % 2 == 0
    message = ("+Even" if is_even else "-Odd")
    state["message"] = message

def _set_up_map(state):

    _headers = {
        "Client-Identifier": credentials["user_id"]
    }
    response = get_all_stations(_headers)
    stations = response['data']['stations']

    df = pd.DataFrame(stations)

    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        zoom=13,
        center={"lat": 59.9139, "lon": 10.7522},  # Oslo coordinates
        title="Bike Sharing Stations"
    )

    state["bike_map"] = fig

    
# Initialise the state

# "_my_private_element" won't be serialised or sent to the frontend,
# because it starts with an underscore

initial_state = wf.init_state({
    "my_app": {
        "title": "MY APP"
    },
    "_my_private_element": 1337,
    "message": None,
    "counter": 26,
})

_update_message(initial_state)
_set_up_map(initial_state)
import requests


_stations_link = "https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json"

def get_all_stations(headers) -> dict:
    response = requests.get(_stations_link, headers=headers)
    return response.json()

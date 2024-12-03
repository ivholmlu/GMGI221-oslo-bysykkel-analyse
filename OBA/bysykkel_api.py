import requests

#Links
_stations_link = "https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json"
_availability_link = "https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json"

def get_all_stations(headers) -> dict:
    response = requests.get(_stations_link, headers=headers)
    return response.json()

def get_bike_info(headers) -> dict:
    response = requests.get(_availability_link, headers=headers)
    return response.json()
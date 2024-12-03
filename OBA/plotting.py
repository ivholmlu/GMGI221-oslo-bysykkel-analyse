from geopandas import GeoDataFrame
import plotly.express as px
import pandas as pd


def generate_bike_stat(stations_gdf : GeoDataFrame, gdf_bydeler) -> list[tuple]:
    """Calculate inhabitants per bike for each bydel

    Args:
        stations_gdf (GeoDataFrame): Dataframe containing 'bydel' and 'num_bikes_available' columns
        gdf_bydeler (GeoDataFrame): Dataframe containing 'bydel' and 'befolkning_2024' columns

    Returns:
        list[tuple]: List of tuples containing the bydel and the average bikes per station
    """

    info = []
    for _, row in gdf_bydeler.iterrows():
        bydel = row["bydel"]
        # Get the number of bikes in the bydel
        bikes_in_bydel = stations_gdf[stations_gdf["bydel"] == bydel]["num_bikes_available"].sum()
        # Calculate the inhabitants per bike
        inhabitants_per_bike = row["befolkning_2024"] / bikes_in_bydel
        if inhabitants_per_bike == float('inf'):
            inhabitants_per_bike = 0
        info.append((bydel, inhabitants_per_bike))
    bike_stat_df = pd.DataFrame(info, columns=['District', 'Inhabitants per Bike'])
    fig = px.bar(
    bike_stat_df,
    x='District',
    y='Inhabitants per Bike',
    title='Inhabitants per Bike by District',
    labels={'District': 'District', 'Inhabitants per Bike': 'Inhabitants per Bike'},)
    return fig

def generate_area_stat(arealer_gdf : GeoDataFrame) -> list[tuple]:
    """Calculate the average area per station for each bydel

    Args:
        gdf_bydeler_non_empty (GeoDataFrame): Dataframe containing 'bydel' and 'geometry' columns

    Returns:
        list[tuple]: List of tuples containing the bydel and the average area per station in square kilometers
    """
    info = []
    #Converting to CRS to calculate the area in square kilometers.
    #Only on local variable, to avoid making the change to a global.
    arealer_gdf_25832 = arealer_gdf.to_crs(epsg=25832)

    for _, row in arealer_gdf_25832.iterrows():
        bydel = row["bydel"]
        area_per_station = (row["geometry"].area / 1e6) / row["point_count"]
        info.append((bydel, area_per_station))

    area_stat_df = pd.DataFrame(info, columns=['District', 'Area per Station (km²)'])
    # Create Plotly Bar Plot
    fig = px.bar(
        area_stat_df,
        x='District',
        y='Area per Station (km²)',
        title='Average Area per Station by District',
        labels={'District': 'District', 'Area per Station (km²)': 'Average Area per Station (km²)'},
    )
    return fig

def generate_stat_avg_(arealer_gdf)->list[tuple]:
    """Calculate the average habitants per station for each bydel

    Args:
        arealer_gdf (GeoDataFrame): Dataframe containing 'bydel' and 'befolkning_2024' columns

    Returns:
        list[tuple]:
        List of tuples containing the bydel and the average habitants per station
    """
    
    info = []
    for _, row in arealer_gdf.iterrows():
        # Calculate the average habitants per station
        bydel = row["bydel"]
        habitants_per_station = row["befolkning_2024"] / row["point_count"]
        # Append the tuple to the list
        info.append((bydel, habitants_per_station))
    
    avg_hab_df = pd.DataFrame(info, columns=['District', 'Average Habitation'])
    fig = px.bar(
    avg_hab_df,
    x='District',
    y='Average Habitation',
    title='Average Habitation by District',
    labels={'District': 'District', 'Average Habitation': 'Average Habitation'},
)
    return fig

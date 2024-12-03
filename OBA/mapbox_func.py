import plotly.graph_objects as go
from geopandas import GeoDataFrame

def highlight_area(fig: go.Figure, arealer_gdf: GeoDataFrame, selected_bydel: str) -> go.Figure:
    """Update the map to highlight a specific area without re-adding markers.

    Args:
        fig (go.Figure): Existing Plotly figure.
        arealer_gdf (GeoDataFrame): GeoDataFrame containing polygons for districts.
        selected_bydel (str): The district to highlight.

    Returns:
        go.Figure: Updated figure with the selected area highlighted.
    """
    for i, feature in enumerate(arealer_gdf.itertuples()):
        geometry = feature.geometry
        lon, lat = [], []
        for poly in geometry.geoms:  # Assuming MultiPolygon geometries
            lon, lat = poly.exterior.xy

        # Determine if this feature matches the selected district
        if feature.bydel == selected_bydel:
            fig.data[i].line.color = 'red'
            fig.data[i].fillcolor = 'rgba(255, 0, 0, 0.3)'
        else:
            fig.data[i].line.color = 'blue'
            fig.data[i].fillcolor = 'rgba(0, 128, 255, 0.1)'

    return fig

def set_up_map(arealer_gdf : GeoDataFrame, stations_gdf : GeoDataFrame) -> go.Figure:
    fig = go.Figure()
    for _, feature in arealer_gdf.iterrows():
        geometry = feature['geometry']
        lon_list = []
        lat_list = []
        for poly in geometry.geoms:
            lon, lat = poly.exterior.xy
            lon_list.append(lon)
            lat_list.append(lat)
        
        fig.add_trace(go.Scattermapbox(
            lon=list(lon),  #
            lat=list(lat),  
            mode='lines',
            line=dict(color='blue', width=2),
            fill='toself',
            fillcolor='rgba(0, 128, 255, 0.1)',
            name=feature['bydel'],
            text = f"<b>{feature['bydel']}</b><br>Population: {feature['befolkning_2024']}",
            hoverinfo='text'
            
            ))

    for _, station in stations_gdf.iterrows():
        fig.add_trace(go.Scattermapbox(
            lat=[station['lat']],
            lon=[station['lon']],
            mode='markers',
            marker=dict(
                size=12,
                color='red',
                opacity=0.8,
            ),
            text=f"<b>{station['name']}</b><br>Available bikes: {station['num_bikes_available']}",
            hoverinfo='text'
        ))

    fig.update_layout(
        mapbox=dict(
            style="carto-positron",  # Choose your preferred Mapbox style
            center=dict(lat=59.91, lon=10.75),  # Center the map on Oslo
            zoom=11
        ),
        margin=dict(l=0, r=0, t=0, b=0),  # Remove extra margins
        height=600,
        title="Oslo Bike Stations and Districts",
        dragmode='zoom',
        showlegend=False,
    )
    return fig



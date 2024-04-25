import geopandas as gpd

gpd.default_crs = 'epsg:4326'

def set_crs(gdf):
    gdf.crs = gpd.default_crs
    return gdf


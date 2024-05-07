# Usage: set_crs(gdf); Sets crs to standarized projection

import geopandas as gpd

gpd.default_crs = 'epsg:4269'

def set_crs(gdf):
    gdf.crs = gpd.default_crs
    return gdf


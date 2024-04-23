import geopandas as gpd

gpd.default_crs = {'init': 'epsg:4269'}

def set_crs(gdf):
    gdf.crs = gpd.default_crs
    return gdf.head(0)


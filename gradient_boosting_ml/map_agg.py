import geopandas as gpd
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
from rasterstats import zonal_stats
import pandas as pd
import numpy as np
import os 

#%%
# zonal statistics
abspath_curr = 'D:/GWU/ML4DAM/'
in_raster = f'{abspath_curr}/data/accra/result/map/XGBoost_subset_230118125708.tif'

# load grid
in_zones =  f'{abspath_curr}/data/accra/acc_SHP/test_grid_100m.geoJSON'
grid = gpd.read_file(f'{abspath_curr}/data/accra/acc_SHP/test_grid_100m.geoJSON')
shp = gpd.read_file(in_zones)
shp.drop(['left', 'top', 'right', 'bottom'], axis=1, inplace=True)


# def zonal_stats(in_raster, in_zones, missng_value=-9999, agg_method='max'):
#     name='max'
#     col_count = 0
#     for file in in_raster:
#%%
zone = zonal_stats(in_zones, in_raster, stats="median", nodata=-9999)
data = pd.DataFrame(zone)
# data.columns = 'max'

# %%
data.head()
# %%

gdf1 = gpd.GeoDataFrame(data)
#%%

shp_out = f'{abspath_curr}/data/accra/result/map/100m_grid.geojson'

gdf = pd.concat([shp, gdf1], axis=1)
gdf.to_file(shp_out, driver='GeoJSON')
# %%

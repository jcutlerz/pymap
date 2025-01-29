#%%

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from geodatasets import get_path

df = pd.DataFrame(
    {
        "City": ["Buenos Aires", "Brasilia", "Santiago", "Bogota", "Caracas"],
        "Country": ["Argentina", "Brazil", "Chile", "Colombia", "Venezuela"],
        "Latitude": [-34.58, -15.78, -33.45, 4.60, 10.48],
        "Longitude": [-58.66, -47.91, -70.66, -74.08, -66.86],
    }
)

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326") # type: ignore

print(gdf.head())

world = gpd.read_file(get_path("naturalearth.land"))

# restrict to South America.
ax = world.clip([-90, -55, -25, 15]).plot(color="white", edgecolor="black")

gdf.plot(ax=ax, color="red")

plt.show()

# %%

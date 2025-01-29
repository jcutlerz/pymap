#%%

import geopandas as gpd
import libpysal

#%%

# va county map comes already installed
dbf = libpysal.io.open(libpysal.examples.get_path("virginia.dbf"))
dbf.header

# %%

libpysal.examples.explain('virginia')

# %%

data = gpd.read_file(libpysal.examples.get_path("virginia.shp"))
type(data)
data.head()

# %%

data.plot()

# %%
